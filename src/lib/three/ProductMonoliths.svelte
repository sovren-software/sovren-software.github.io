<script>
  // @ts-nocheck
  import { onMount, onDestroy } from 'svelte';
  import * as THREE from 'three';
  import { browser } from '$app/environment';
  import gsap from 'gsap';

  export let products = [];

  let canvas;
  let renderer, scene, camera;
  let monoliths = [];
  let raycaster, mouse;
  let animationFrame;
  let themeObserver;
  let mediaQuery;
  let isDarkMode = false;

  function checkTheme() {
    isDarkMode = document.documentElement.getAttribute('data-theme') === 'dark' ||
                (!document.documentElement.hasAttribute('data-theme') && window.matchMedia('(prefers-color-scheme: dark)').matches);

    updateMonolithColors();
  }

  function updateMonolithColors() {
    const baseColor = isDarkMode ? 0x555555 : 0x333333; // Darker gray for light mode
    monoliths.forEach(m => {
      if (!m.isHovered) {
        const targetColor = new THREE.Color(baseColor);
        gsap.to(m.material.color, {
          r: targetColor.r,
          g: targetColor.g,
          b: targetColor.b,
          duration: 0.5
        });
      }
    });
  }

  onMount(() => {
    if (!browser) return;

    // Theme awareness
    mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    mediaQuery.addEventListener('change', checkTheme);

    themeObserver = new MutationObserver((mutations) => {
      mutations.forEach((mutation) => {
        if (mutation.attributeName === 'data-theme') checkTheme();
      });
    });

    themeObserver.observe(document.documentElement, { attributes: true });
    checkTheme();

    // Setup
    scene = new THREE.Scene();

    const width = canvas.clientWidth;
    const height = canvas.clientHeight;

    camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 100);
    camera.position.z = 15;

    renderer = new THREE.WebGLRenderer({
      canvas,
      alpha: true,
      antialias: true
    });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    raycaster = new THREE.Raycaster();
    mouse = new THREE.Vector2();

    // Create monoliths
    const geometry = new THREE.BoxGeometry(3, 5, 0.5);
    const edges = new THREE.EdgesGeometry(geometry);

    products.forEach((p, i) => {
      // Group for holding the wireframe and any interaction state
      const group = new THREE.Group();

      // Wireframe
      const baseColor = isDarkMode ? 0x555555 : 0x333333;
      const material = new THREE.LineBasicMaterial({
        color: baseColor,
        transparent: true,
        opacity: 0.8
      });
      const lines = new THREE.LineSegments(edges, material);
      group.add(lines);

      // Invisible mesh for raycasting
      const hitMesh = new THREE.Mesh(
        geometry,
        new THREE.MeshBasicMaterial({ visible: false })
      );
      hitMesh.userData = { index: i };
      group.add(hitMesh);

      // Positioning
      const offset = (i - 1) * 4; // Assuming 3 products
      group.position.x = offset;
      group.position.y = -2; // Start below

      // Intro animation
      gsap.to(group.position, {
        y: 0,
        duration: 2,
        delay: i * 0.2 + 0.5,
        ease: "power3.out"
      });

      scene.add(group);
      monoliths.push({
        group,
        lines,
        material,
        originalY: 0,
        originalX: offset,
        isHovered: false
      });
    });

    // Initial color sync
    updateMonolithColors();

    // Listeners
    window.addEventListener('resize', onResize);
    canvas.addEventListener('mousemove', onMouseMove);
    canvas.addEventListener('mouseleave', onMouseLeave);

    // Animation loop
    const tick = () => {
      // Subtle floating
      const time = Date.now() * 0.001;
      monoliths.forEach((m, i) => {
        if (!m.isHovered) {
          m.group.position.y = Math.sin(time + i) * 0.1;
          m.group.rotation.y = Math.sin(time * 0.5 + i) * 0.05;
        }
      });

      renderer.render(scene, camera);
      animationFrame = requestAnimationFrame(tick);
    };

    tick();
  });

  function onResize() {
    if (!camera || !renderer || !canvas) return;
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height);
  }

  function onMouseMove(event) {
    const rect = canvas.getBoundingClientRect();
    mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
    mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

    raycaster.setFromCamera(mouse, camera);
    const intersects = raycaster.intersectObjects(scene.children, true);

    let hoveredIndex = -1;
    if (intersects.length > 0) {
      const hit = intersects.find(i => i.object.userData.index !== undefined);
      if (hit) hoveredIndex = hit.object.userData.index;
    }

    monoliths.forEach((m, i) => {
      const isHovered = i === hoveredIndex;
      if (isHovered !== m.isHovered) {
        m.isHovered = isHovered;

        // Tilt and glow effect
        gsap.to(m.group.rotation, {
          x: isHovered ? -0.1 : 0,
          y: isHovered ? 0.2 : 0,
          duration: 0.8,
          ease: "power2.out"
        });

        gsap.to(m.group.position, {
          z: isHovered ? 1 : 0,
          y: isHovered ? 0.5 : 0,
          duration: 0.8,
          ease: "power2.out"
        });

        // Color transition
        const hoverColor = isDarkMode ? 0xffffff : 0x000000;
        const baseColor = isDarkMode ? 0x555555 : 0x333333;
        const targetColor = new THREE.Color(isHovered ? hoverColor : baseColor);

        gsap.to(m.material.color, {
          r: targetColor.r,
          g: targetColor.g,
          b: targetColor.b,
          duration: 0.5
        });

        // Dispatch event for UI updates if needed
        if (isHovered) {
          canvas.dispatchEvent(new CustomEvent('monolith-hover', { detail: { index: i } }));
        }
      }
    });
  }

  function onMouseLeave() {
    monoliths.forEach(m => {
      m.isHovered = false;
      gsap.to(m.group.rotation, { x: 0, y: 0, duration: 0.8 });
      gsap.to(m.group.position, { z: 0, duration: 0.8 });

      const baseColor = isDarkMode ? 0x555555 : 0x333333;
      const targetColor = new THREE.Color(baseColor);
      gsap.to(m.material.color, {
        r: targetColor.r,
        g: targetColor.g,
        b: targetColor.b,
        duration: 0.5
      });
    });
  }

  onDestroy(() => {
    if (!browser) return;
    window.removeEventListener('resize', onResize);
    if (canvas) {
      canvas.removeEventListener('mousemove', onMouseMove);
      canvas.removeEventListener('mouseleave', onMouseLeave);
    }
    cancelAnimationFrame(animationFrame);
    if (renderer) renderer.dispose();
  });
</script>

<canvas bind:this={canvas} class="monolith-canvas"></canvas>

<style>
  .monolith-canvas {
    width: 100%;
    height: 600px;
    display: block;
  }
</style>
