// @ts-nocheck
import * as THREE from 'three';

export class SceneManager {
  constructor(canvas) {
    this.canvas = canvas;

    // WebGL support check
    if (!this.isWebGLAvailable()) {
      console.warn('WebGL is not available on this device/browser');
      this.webglAvailable = false;
      return;
    }

    this.webglAvailable = true;
    this.width = window.innerWidth;
    this.height = window.innerHeight;

    this.scene = new THREE.Scene();
    this.scene.fog = new THREE.FogExp2(0xffffff, 0.02); // White fog for light theme

    this.camera = new THREE.PerspectiveCamera(45, this.width / this.height, 0.1, 1000);
    // Camera starts pulled back a bit
    this.camera.position.set(0, 0, 15);

    this.renderer = new THREE.WebGLRenderer({
      canvas: this.canvas,
      antialias: true,
      alpha: true,
      powerPreference: "default"
    });
    this.renderer.setSize(this.width, this.height);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    this.clock = new THREE.Clock();
    this.scrollY = 0;
    this.mouse = new THREE.Vector2(0, 0);
    this.targetMouse = new THREE.Vector2(0, 0);

    this.initScene();

    // Theme awareness
    this.updateThemeColors = this.updateThemeColors.bind(this);
    this.themeObserver = new MutationObserver((mutations) => {
      mutations.forEach((mutation) => {
        if (mutation.attributeName === 'data-theme') {
          this.updateThemeColors();
        }
      });
    });

    this.themeObserver.observe(document.documentElement, {
      attributes: true
    });

    // Also listen for system preference changes
    this.mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    this.mediaQuery.addEventListener('change', this.updateThemeColors);

    // Initial color setup
    this.updateThemeColors();

    this.reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    this.reducedMotionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    this.onReducedMotionChange = (e) => { this.reducedMotion = e.matches; };
    this.reducedMotionQuery.addEventListener('change', this.onReducedMotionChange);

    this.addListeners();

    this.tick = this.tick.bind(this);
    this.tick();
  }

  updateThemeColors() {
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark' ||
                  (!document.documentElement.hasAttribute('data-theme') && window.matchMedia('(prefers-color-scheme: dark)').matches);

    const fogColor = isDark ? 0x000000 : 0xffffff;
    const wireColor = isDark ? 0xffffff : 0x000000;
    const gridColor1 = isDark ? 0x444444 : 0x888888; // Darker grid for light mode
    const gridColor2 = isDark ? 0x222222 : 0xcccccc;

    if (this.scene.fog instanceof THREE.FogExp2) {
      this.scene.fog.color.setHex(fogColor);
      this.scene.fog.density = isDark ? 0.02 : 0.015;
    } else if (this.scene.fog instanceof THREE.Fog) {
      this.scene.fog.color.setHex(fogColor);
    }

    if (this.cubeMaterial) this.cubeMaterial.color.setHex(wireColor);
    if (this.innerShape) this.innerShape.material.color.setHex(wireColor);

    if (this.grid) {
      const posZ = this.grid.position.z;
      this.scene.remove(this.grid);
      this.grid = new THREE.GridHelper(100, 100, gridColor1, gridColor2);
      this.grid.position.y = -5;
      this.grid.position.z = posZ;
      this.scene.add(this.grid);
    }

    if (this.particles) {
      this.particles.material.color.setHex(wireColor);
      this.particles.material.opacity = isDark ? 0.4 : 0.2; // Softer particles in light mode
    }
  }

  isWebGLAvailable() {
    try {
      const canvas = document.createElement('canvas');
      return !!(window.WebGLRenderingContext && (canvas.getContext('webgl') || canvas.getContext('experimental-webgl')));
    } catch {
      return false;
    }
  }

  initScene() {
    // 1. Massive floating wireframe cube (ASCII-inspired geometry)
    const geometry = new THREE.BoxGeometry(4, 4, 4);
    const edges = new THREE.EdgesGeometry(geometry);

    // Custom shader material for the bloom/glow effect on wireframe
    this.cubeMaterial = new THREE.LineBasicMaterial({
      color: 0x000000, // Black lines for light theme
      transparent: true,
      opacity: 0.6,
      depthWrite: false,
    });

    this.cube = new THREE.LineSegments(edges, this.cubeMaterial);
    this.cube.rotation.set(Math.PI / 4, Math.PI / 4, 0);
    this.scene.add(this.cube);

    // Add some inner geometry for depth
    const innerGeo = new THREE.OctahedronGeometry(2);
    const innerEdges = new THREE.EdgesGeometry(innerGeo);
    this.innerShape = new THREE.LineSegments(innerEdges, new THREE.LineBasicMaterial({
      color: 0x000000, // Black lines for light theme
      transparent: true,
      opacity: 0.2,
      depthWrite: false
    }));
    this.cube.add(this.innerShape);

    // 2. Background 3D grid plane extending into infinity
    const gridHelper = new THREE.GridHelper(100, 100, 0xcccccc, 0xeeeeee); // Light grid
    gridHelper.position.y = -5;
    gridHelper.position.z = -10;
    this.scene.add(gridHelper);
    this.grid = gridHelper;

    // 3. Volumetric light shafts / dust particles
    const particleGeo = new THREE.BufferGeometry();
    const particleCount = 500;
    const posArray = new Float32Array(particleCount * 3);
    for(let i=0; i < particleCount * 3; i++) {
      posArray[i] = (Math.random() - 0.5) * 40;
    }
    particleGeo.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
    const particleMat = new THREE.PointsMaterial({
      size: 0.05,
      color: 0x000000, // Black particles for light theme
      transparent: true,
      opacity: 0.2,
      blending: THREE.NormalBlending
    });
    this.particles = new THREE.Points(particleGeo, particleMat);
    this.scene.add(this.particles);
  }

  addListeners() {
    this._onResize = this.onResize.bind(this);
    this._onScroll = this.onScroll.bind(this);
    this._onMouseMove = this.onMouseMove.bind(this);
    window.addEventListener('resize', this._onResize);
    window.addEventListener('scroll', this._onScroll);
    window.addEventListener('mousemove', this._onMouseMove);
  }

  onResize() {
    this.width = window.innerWidth;
    this.height = window.innerHeight;
    this.camera.aspect = this.width / this.height;
    this.camera.updateProjectionMatrix();
    this.renderer.setSize(this.width, this.height);
  }

  onScroll() {
    this.scrollY = window.scrollY;
  }

  onMouseMove(e) {
    this.targetMouse.x = (e.clientX / this.width) * 2 - 1;
    this.targetMouse.y = -(e.clientY / this.height) * 2 + 1;
  }

  tick() {
    const elapsedTime = this.clock.getElapsedTime();

    // Smooth mouse interpolation
    this.mouse.x += (this.targetMouse.x - this.mouse.x) * 0.05;
    this.mouse.y += (this.targetMouse.y - this.mouse.y) * 0.05;

    if (!this.reducedMotion) {
      // Slow, deliberate rotation for the central cube
      if (this.cube) {
        this.cube.rotation.y += 0.002;
        this.cube.rotation.x += 0.001;
        this.cube.position.y = Math.sin(elapsedTime * 0.5) * 0.2;
      }

      if (this.innerShape) {
        this.innerShape.rotation.y -= 0.003;
        this.innerShape.rotation.x -= 0.002;
      }

      // Grid animation (moving forward to simulate descending)
      if (this.grid) {
        this.grid.position.z = (elapsedTime * 0.5) % 1 - 10;
      }

      // Particles slow drift
      if (this.particles) {
        this.particles.rotation.y = elapsedTime * 0.02;
      }
    }

    // Scroll-based camera animation (cinematic drift and descent)
    // Map scroll to camera Z and Y, tilting slightly
    const scrollProgress = this.scrollY / (document.body.scrollHeight - this.height || 1);

    if (!this.reducedMotion) {
      // Ease the camera position
      const targetCamZ = 15 - (scrollProgress * 20);
      const targetCamY = -(scrollProgress * 5);

      this.camera.position.z += (targetCamZ - this.camera.position.z) * 0.05;
      this.camera.position.y += (targetCamY - this.camera.position.y) * 0.05;

      // Parallax from mouse (subtle)
      this.camera.position.x += (this.mouse.x * 0.5 - this.camera.position.x) * 0.05;

      // Camera look target shifts slightly based on scroll
      const lookAtTarget = new THREE.Vector3(
        this.mouse.x * 0.2,
        -(scrollProgress * 2) + this.mouse.y * 0.2,
        0
      );
      this.camera.lookAt(lookAtTarget);
    }

    this.renderer.render(this.scene, this.camera);
    this.animationFrame = requestAnimationFrame(this.tick);
  }

  destroy() {
    if (!this.webglAvailable) return;
    cancelAnimationFrame(this.animationFrame);
    window.removeEventListener('resize', this._onResize);
    window.removeEventListener('scroll', this._onScroll);
    window.removeEventListener('mousemove', this._onMouseMove);

    if (this.themeObserver) this.themeObserver.disconnect();
    if (this.mediaQuery) this.mediaQuery.removeEventListener('change', this.updateThemeColors);
    if (this.reducedMotionQuery) this.reducedMotionQuery.removeEventListener('change', this.onReducedMotionChange);

    // Dispose geometries and materials to prevent GPU memory leaks
    this.scene.traverse((obj) => {
      if (obj instanceof THREE.Mesh || obj instanceof THREE.LineSegments || obj instanceof THREE.Points) {
        if (obj.geometry) obj.geometry.dispose();
        if (obj.material) {
          if (Array.isArray(obj.material)) obj.material.forEach(m => m.dispose());
          else obj.material.dispose();
        }
      }
    });

    if (this.renderer) {
      this.renderer.dispose();
      this.renderer.forceContextLoss();
    }
  }
}
