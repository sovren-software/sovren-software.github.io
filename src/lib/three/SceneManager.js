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
    this.scene.fog = new THREE.FogExp2(0x000000, 0.02);

    this.camera = new THREE.PerspectiveCamera(45, this.width / this.height, 0.1, 1000);
    // Camera starts pulled back a bit
    this.camera.position.set(0, 0, 15);

    this.renderer = new THREE.WebGLRenderer({
      canvas: this.canvas,
      antialias: true,
      alpha: true,
      powerPreference: "high-performance"
    });
    this.renderer.setSize(this.width, this.height);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    this.clock = new THREE.Clock();
    this.scrollY = 0;
    this.mouse = new THREE.Vector2(0, 0);
    this.targetMouse = new THREE.Vector2(0, 0);

    this.initScene();
    this.addListeners();

    this.tick = this.tick.bind(this);
    this.tick();
  }

  isWebGLAvailable() {
    try {
      const canvas = document.createElement('canvas');
      return !!(window.WebGLRenderingContext && (canvas.getContext('webgl') || canvas.getContext('experimental-webgl')));
    } catch (e) {
      return false;
    }
  }

  initScene() {
    // 1. Massive floating wireframe cube (ASCII-inspired geometry)
    const geometry = new THREE.BoxGeometry(4, 4, 4);
    const edges = new THREE.EdgesGeometry(geometry);
    
    // Custom shader material for the bloom/glow effect on wireframe
    this.cubeMaterial = new THREE.LineBasicMaterial({
      color: 0xffffff,
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
      color: 0xffffff,
      transparent: true,
      opacity: 0.2,
      depthWrite: false
    }));
    this.cube.add(this.innerShape);

    // 2. Background 3D grid plane extending into infinity
    const gridHelper = new THREE.GridHelper(100, 100, 0x333333, 0x111111);
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
      color: 0xffffff,
      transparent: true,
      opacity: 0.4,
      blending: THREE.AdditiveBlending
    });
    this.particles = new THREE.Points(particleGeo, particleMat);
    this.scene.add(this.particles);
  }

  addListeners() {
    window.addEventListener('resize', this.onResize.bind(this));
    window.addEventListener('scroll', this.onScroll.bind(this));
    window.addEventListener('mousemove', this.onMouseMove.bind(this));
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
    const deltaTime = this.clock.getDelta();

    // Smooth mouse interpolation
    this.mouse.x += (this.targetMouse.x - this.mouse.x) * 0.05;
    this.mouse.y += (this.targetMouse.y - this.mouse.y) * 0.05;

    // Slow, deliberate rotation for the central cube
    if (this.cube) {
      this.cube.rotation.y += 0.002;
      this.cube.rotation.x += 0.001;
      this.cube.position.y = Math.sin(elapsedTime * 0.5) * 0.2; // Subtle floating
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

    // Scroll-based camera animation (cinematic drift and descent)
    // Map scroll to camera Z and Y, tilting slightly
    const scrollProgress = this.scrollY / (document.body.scrollHeight - this.height || 1);
    
    // Ease the camera position
    const targetCamZ = 15 - (scrollProgress * 20); // Move forward as we scroll down
    const targetCamY = - (scrollProgress * 5); // Descend slightly
    
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

    this.renderer.render(this.scene, this.camera);
    this.animationFrame = requestAnimationFrame(this.tick);
  }

  destroy() {
    if (!this.webglAvailable) return;
    cancelAnimationFrame(this.animationFrame);
    window.removeEventListener('resize', this.onResize.bind(this));
    window.removeEventListener('scroll', this.onScroll.bind(this));
    window.removeEventListener('mousemove', this.onMouseMove.bind(this));
    if (this.renderer) this.renderer.dispose();
  }
}
