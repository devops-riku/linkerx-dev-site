<template>
    <!-- About Section with Vuetify -->
    <section id="about" class="about-section py-14 position-relative">
      <!-- Background Elements -->
      <div class="tech-background"></div>
      
      <v-container>
        <v-row align="center">
          <v-col cols="12" md="6">
            <div class="about-content">
              <v-sheet
                class="mb-4 pa-0"
                color="transparent"
              >
                <div class="section-title d-flex align-center">
                  <div class="section-accent mr-3 bg-gradient-primary"></div>
                  <h2 class="text-h5 font-weight-light mb-0">About Us</h2>
                </div>
              </v-sheet>
              
              <!-- Main Content -->
              <p class="text-body-1 text-medium-emphasis mb-4">
                We are developers, designers, and cloud experts passionate about building products that move businesses forward.
              </p>
              
              <!-- Highlighted Text -->
              <v-sheet
                class="mb-6 pa-4 rounded-lg border-l-primary text-enhancement"
                elevation="1"
                :color="theme.current.value.colors.surface"
              >
                <p class="text-body-2 mb-0">
                  Leveraging cutting-edge technologies to create solutions that are both powerful and user-friendly.
                </p>
              </v-sheet>
              
              <!-- Stats -->
              <v-row class="mt-6">
                <v-col v-for="(stat, i) in stats" :key="i" cols="6">
                  <v-hover v-slot="{ isHovering, props }">
                    <v-card
                      v-bind="props"
                      :elevation="isHovering ? 4 : 0"
                      :class="{'on-hover': isHovering}"
                      rounded="lg"
                      class="stat-card pa-4 text-center"
                      color="transparent"
                    >
                      <div :class="`text-gradient-${i+1} text-h5 font-weight-medium mb-1`">
                        {{ stat.value }}
                      </div>
                      <div class="text-caption">
                        {{ stat.label }}
                      </div>
                      <v-divider class="my-2 stat-divider"></v-divider>
                    </v-card>
                  </v-hover>
                </v-col>
              </v-row>
            </div>
          </v-col>
          
          <v-col cols="12" md="6">
            <v-hover v-slot="{ isHovering, props }">
              <v-card
                v-bind="props"
                class="image-container pa-0 rounded-lg"
                :elevation="isHovering ? 16 : 8"
                :class="{'on-hover': isHovering}"
                style="overflow: hidden; transform-style: preserve-3d"
                ref="imageCard"
              >
                <!-- Image -->
                <v-img
                  src="https://cdn.pixabay.com/photo/2016/11/18/18/37/programming-1836330_1280.png"
                  height="333"
                  cover
                  class="image-zoom"
                >
                  <template v-slot:placeholder>
                    <v-row class="fill-height ma-0" align="center" justify="center">
                      <v-progress-circular indeterminate color="primary"></v-progress-circular>
                    </v-row>
                  </template>
                  
                  <!-- Overlay with Animation -->
                  <div class="image-overlay"></div>
                </v-img>
                
                <!-- Corner Accents -->
                <div class="corner-accent top-left"></div>
                <div class="corner-accent top-right"></div>
                <div class="corner-accent bottom-left"></div>
                <div class="corner-accent bottom-right"></div>
                
                <!-- Tech Scan Animation -->
                <div class="tech-scan-line"></div>
              </v-card>
            </v-hover>
          </v-col>
        </v-row>
      </v-container>
    </section>
  </template>
  
  <script setup>
  import { ref, onMounted, onUnmounted } from 'vue'
  import { useTheme } from 'vuetify'
  
  const theme = useTheme()
  const imageCard = ref(null)
  
  const stats = [
    { value: '5+', label: 'Projects Delivered' },
    { value: '98%', label: 'Client Satisfaction' },
    { value: '7+', label: 'Years Experience' }
  ]
  
  // Handle 3D rotation effect on image card
  onMounted(() => {
    if (window.innerWidth > 960) {
      const card = imageCard.value?.$el
      if (!card) return
      
      // Mouse tracking logic for 3D effect
      const handleMouseMove = (e) => {
        if (!card) return
        
        const rect = card.getBoundingClientRect()
        const x = e.clientX - rect.left
        const y = e.clientY - rect.top
        
        const centerX = rect.width / 2
        const centerY = rect.height / 2
        
        const rotateX = (y - centerY) / 20
        const rotateY = (centerX - x) / 20
        
        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`
      }
      
      const handleMouseLeave = () => {
        card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale3d(1, 1, 1)'
      }
      
      // Add particle elements to background
      addParticleElements()
      
      card.addEventListener('mousemove', handleMouseMove)
      card.addEventListener('mouseleave', handleMouseLeave)
      
      onUnmounted(() => {
        card.removeEventListener('mousemove', handleMouseMove)
        card.removeEventListener('mouseleave', handleMouseLeave)
      })
    }
  })
  
  // Create dynamic particle elements
  function addParticleElements() {
    const section = document.querySelector('.about-section')
    if (!section) return
    
    // Create floating particles
    for (let i = 0; i < 10; i++) {
      const particle = document.createElement('div')
      particle.classList.add('floating-particle')
      
      const size = 3 + Math.random() * 3
      
      particle.style.width = `${size}px`
      particle.style.height = `${size}px`
      particle.style.left = `${Math.random() * 100}%`
      particle.style.top = `${Math.random() * 100}%`
      particle.style.animationDuration = `${5 + Math.random() * 15}s`
      particle.style.animationDelay = `${Math.random() * 5}s`
      
      section.appendChild(particle)
    }
    
    // Create data stream lines
    for (let i = 0; i < 3; i++) {
      const dataStream = document.createElement('div')
      dataStream.classList.add('data-stream')
      dataStream.style.left = `${20 + i * 25}%`
      dataStream.style.animationDelay = `${i * 2}s`
      section.appendChild(dataStream)
    }
  }
  </script>
  
  <style scoped>
  /* Section Background */
  .about-section {
    overflow: hidden;
    --primary-color: rgb(var(--v-theme-primary));
    --primary-light: rgba(var(--v-theme-primary), 0.2);
    --primary-lighter: rgba(var(--v-theme-primary), 0.1);
    --primary-gradient: linear-gradient(135deg, var(--primary-color), rgb(var(--v-theme-secondary)));
  }
  
  .tech-background {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    background-image: 
      radial-gradient(circle at 25% 30%, var(--primary-lighter) 0%, transparent 40%),
      radial-gradient(circle at 75% 60%, rgba(var(--v-theme-secondary), 0.07) 0%, transparent 40%);
    opacity: 0.7;
  }
  
  /* Background elements */
  .section-accent {
    width: 4px;
    height: 24px;
    border-radius: 2px;
  }
  
  .bg-gradient-primary {
    background: var(--primary-gradient);
  }
  
  /* Text gradients for stats */
  .text-gradient-1, .text-gradient-2, .text-gradient-3 {
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  
  /* Enhancements */
  .text-enhancement {
    border-left: 3px solid var(--primary-color);
    transition: transform 0.3s ease;
  }
  
  .text-enhancement:hover {
    transform: translateX(5px);
  }
  
  /* Stat card effects */
  .stat-card {
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    position: relative;
    overflow: hidden;
  }
  
  .stat-card.on-hover {
    transform: translateY(-5px);
  }
  
  .stat-divider {
    position: relative;
    overflow: hidden;
    background: var(--primary-lighter);
    opacity: 0.5;
  }
  
  .stat-divider::after {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(to right, transparent, #fff, transparent);
    animation: stat-shine 3s ease-in-out infinite;
  }
  
  @keyframes stat-shine {
    0% { left: -100%; }
    100% { left: 100%; }
  }
  
  /* Image card effects */
  .image-container {
    position: relative;
    overflow: hidden;
    transition: all 0.5s cubic-bezier(0.25, 0.8, 0.25, 1);
    transform-style: preserve-3d;
  }
  
  .image-zoom {
    transition: transform 0.5s ease;
  }
  
  .image-container.on-hover .image-zoom {
    transform: scale(1.05);
  }
  
  .image-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, 
      var(--primary-lighter) 0%, 
      transparent 40%, 
      rgba(var(--v-theme-secondary), 0.1) 80%);
    z-index: 1;
  }
  
  /* Corner Accents */
  .corner-accent {
    position: absolute;
    width: 20px;
    height: 20px;
    border-color: var(--primary-color);
    border-style: solid;
    z-index: 2;
    opacity: 0.5;
    transition: all 0.3s ease;
  }
  
  .image-container.on-hover .corner-accent {
    opacity: 0.8;
  }
  
  .top-left {
    top: 0;
    left: 0;
    border-width: 2px 0 0 2px;
    border-radius: 4px 0 0 0;
  }
  
  .top-right {
    top: 0;
    right: 0;
    border-width: 2px 2px 0 0;
    border-radius: 0 4px 0 0;
  }
  
  .bottom-left {
    bottom: 0;
    left: 0;
    border-width: 0 0 2px 2px;
    border-radius: 0 0 0 4px;
  }
  
  .bottom-right {
    bottom: 0;
    right: 0;
    border-width: 0 2px 2px 0;
    border-radius: 0 0 4px 0;
  }
  
  /* Tech Scan Line Animation */
  .tech-scan-line {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background: linear-gradient(to right, transparent, var(--primary-color), transparent);
    z-index: 2;
    opacity: 0;
    animation: scan-line 5s ease-in-out infinite;
  }
  
  @keyframes scan-line {
    0% {
      top: 0;
      opacity: 0;
    }
    10% {
      opacity: 0.8;
    }
    90% {
      opacity: 0.8;
    }
    100% {
      top: 100%;
      opacity: 0;
    }
  }
  
  /* Floating Particles */
  .floating-particle {
    position: absolute;
    border-radius: 50%;
    background-color: var(--primary-color);
    opacity: 0.2;
    z-index: -1;
    animation: float-around linear infinite;
  }
  
  @keyframes float-around {
    0% { transform: translate(0, 0); }
    25% { transform: translate(10px, 10px); }
    50% { transform: translate(0, 20px); }
    75% { transform: translate(-10px, 10px); }
    100% { transform: translate(0, 0); }
  }
  
  /* Data Stream Animation */
  .data-stream {
    position: absolute;
    top: 0;
    width: 1px;
    height: 100%;
    left: 15%;
    background: linear-gradient(to bottom, transparent, var(--primary-color), transparent);
    opacity: 0;
    z-index: -1;
    animation: data-stream 8s linear infinite;
  }
  
  @keyframes data-stream {
    0% {
      opacity: 0;
      transform: translateY(-100%);
    }
    30% {
      opacity: 0.3;
    }
    70% {
      opacity: 0.3;
    }
    100% {
      opacity: 0;
      transform: translateY(100%);
    }
  }
  
  /* Border utility class */
  .border-l-primary {
    border-left: 3px solid var(--primary-color);
  }
  
  /* Adding Vuetify responsive helpers */
  @media (max-width: 960px) {
    .image-container {
      margin-top: 30px;
    }
  }
  </style>