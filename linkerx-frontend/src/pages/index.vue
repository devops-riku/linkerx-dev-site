<template>
  <!-- Fixed AppHeader placed outside of v-app -->
  <AppHeader :menu-items="menuItems" @navigate="handleNavigation" />

  <v-app>
    <!-- Custom Cursor -->
    <div class="custom-cursor" :class="{ 'light-mode': !theme.global.current.value.dark }" ref="customCursor"></div>
    <div class="cursor-dot" :class="{ 'light-mode': !theme.global.current.value.dark }" ref="cursorDot"></div>

    <!-- Abstract Tech Backgrounds -->
    <div class="tech-pattern tech-pattern-1" :class="{ 'light-mode': !theme.global.current.value.dark }"></div>
    <div class="tech-pattern tech-pattern-2" :class="{ 'light-mode': !theme.global.current.value.dark }"></div>
    <div class="tech-pattern tech-pattern-3" :class="{ 'light-mode': !theme.global.current.value.dark }"></div>
    <div class="tech-grid" :class="{ 'light-mode': !theme.global.current.value.dark }"></div>

    <v-main>
      <v-container fluid>
        <!-- Hero Section -->
        <section id="home" class="hero py-14 text-center position-relative overflow-hidden">
          <div class="circuit-lines" :class="{ 'light-mode': !theme.global.current.value.dark }"></div>
          <v-row justify="center">
            <v-col cols="12" md="6 mt-10">
              <h1 class="display-1 font-weight-light mb-4 glitch-text">Innovate. Launch. Scale.</h1>
              <p class="text-body-1 text-medium-emphasis mb-6">
                Tech solutions built to perform — from idea to impact.
              </p>
              <v-btn variant="outlined" size="large" class="tech-btn" @click="scrollToContact">
                <span class="btn-text">Start a Project</span>
                <span class="btn-hover-effect"></span>
              </v-btn>
            </v-col>
          </v-row>
          <div class="floating-tech-elements">
            <div class="tech-element" :class="{ 'light-mode': !theme.global.current.value.dark }" v-for="i in 5" :key="i"></div>
          </div>
        </section>

        <!-- Services Section -->
        <section 
          id="services" 
          class="services py-14 position-relative" 
          :style="{
            backgroundColor: theme.global.current.value.colors.surface,
            color: theme.global.current.value.colors['on-surface']
          }"
        >
          <div class="tech-dots" :class="{ 'light-mode': !theme.global.current.value.dark }"></div>
          <v-container>
            <h2 class="text-center text-h5 font-weight-light mb-10">Our Services</h2>
            <v-row justify="center">
              <v-col cols="12" sm="6" md="4" v-for="(service, i) in services" :key="i">
                <v-card
                  variant="flat"
                  class="pa-6 service-card"
                  :class="{ 'light-mode': !theme.global.current.value.dark }"
                  :style="{
                    backgroundColor: theme.global.current.value.colors.background,
                    color: theme.global.current.value.colors['on-surface']
                  }"
                  elevation="4"
                >
                  <div class="service-icon-wrapper">
                    <Icon :icon="service.icon" width="36" height="36" class="mb-4 service-icon" />
                    <div class="icon-ripple" :class="{ 'light-mode': !theme.global.current.value.dark }"></div>
                  </div>
                  <h3 class="text-h6 font-weight-medium mb-2">{{ service.title }}</h3>
                  <p class="text-body-2 text-medium-emphasis">{{ service.description }}</p>
                  <div class="card-corner-accent" :class="{ 'light-mode': !theme.global.current.value.dark }"></div>
                </v-card>
              </v-col>
            </v-row>
          </v-container>
        </section>

        <!-- About Section -->
        <AboutUs />

        <!-- CTA Section with fixed text color -->
        <section
          id="contact"
          class="cta py-16 text-center position-relative"
          :style="{
            backgroundColor: theme.global.current.value.colors.surface,
            color: theme.global.current.value.dark ? 'white' : theme.global.current.value.colors['on-surface']
          }"
          ref="contactSection"
        >
          <div class="tech-waves" :class="{ 'light-mode': !theme.global.current.value.dark }"></div>
          <h2 class="text-h5 font-weight-light mb-4">Let's Build Something Great</h2>
          <p class="text-body-2 mb-6">We're ready when you are.</p>
          <v-btn
            variant="outlined"
            :color="theme.global.current.value.dark ? 'white' : 'primary'"
            size="large"
            class="tech-contact-btn"
            :class="{ 'light-mode': !theme.global.current.value.dark }"
            :to="{ path: '/contact-us' }"
          >
            Contact Us
            <div class="btn-pulse" :class="{ 'light-mode': !theme.global.current.value.dark }"></div>
          </v-btn>
        </section>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { useTheme } from 'vuetify'
import { Icon } from '@iconify/vue'
import AppHeader from '@/components/AppHeader.vue'
import AboutUs from '@/components/AboutUs.vue'

const theme = useTheme()
const contactSection = ref(null)
const customCursor = ref(null)
const cursorDot = ref(null)

const menuItems = [
  { title: 'Home', target: 'home' },
  { title: 'Services', target: 'services' },
  { title: 'About', target: 'about' }
]

const services = [
  {
    icon: 'mdi-web',
    title: 'Web Development',
    description: 'Fast, secure, and scalable web applications.'
  },
  {
    icon: 'mdi-cellphone',
    title: 'Mobile Apps',
    description: 'Cross-platform mobile solutions.'
  },
  {
    icon: 'mdi-cloud-outline',
    title: 'Cloud Solutions',
    description: 'Cloud-native infrastructure and automation.'
  },
  {
    icon: 'eos-icons:iot',
    title: 'IOT Solutions',
    description: 'Seamless connectivity—powered by IoT.'
  },
  {
    icon: 'mdi-api',
    title: 'API Development',
    description: 'Build and connect RESTful APIs for your platform.'
  }
]

const scrollToContact = () => {
  contactSection.value?.scrollIntoView({ behavior: 'smooth' })
}

const handleNavigation = (id) => {
  const el = document.getElementById(id)
  if (el) el.scrollIntoView({ behavior: 'smooth' })
}

// Cursor logic
onMounted(() => {
  window.addEventListener('mousemove', updateCursor)
  document.addEventListener('mousedown', expandCursor)
  document.addEventListener('mouseup', shrinkCursor)
  
  // Initialize floating tech elements animation
  animateFloatingElements()
  
  // Initialize tech wave animation
  animateTechWaves()
})

onUnmounted(() => {
  window.removeEventListener('mousemove', updateCursor)
  document.removeEventListener('mousedown', expandCursor)
  document.removeEventListener('mouseup', shrinkCursor)
})

function updateCursor(e) {
  if (customCursor.value && cursorDot.value) {
    customCursor.value.style.left = `${e.clientX}px`
    customCursor.value.style.top = `${e.clientY}px`
    cursorDot.value.style.left = `${e.clientX}px`
    cursorDot.value.style.top = `${e.clientY}px`
  }
}

function expandCursor() {
  if (customCursor.value) {
    customCursor.value.style.width = '36px'
    customCursor.value.style.height = '36px'
    customCursor.value.style.backgroundColor = theme.global.current.value.dark ? 
      'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)'
  }
}

function shrinkCursor() {
  if (customCursor.value) {
    customCursor.value.style.width = '20px'
    customCursor.value.style.height = '20px'
    customCursor.value.style.backgroundColor = 'transparent'
  }
}

function animateFloatingElements() {
  const elements = document.querySelectorAll('.tech-element')
  elements.forEach((el, i) => {
    const delay = i * 0.8
    const duration = 3 + Math.random() * 4
    
    el.style.animationDelay = `${delay}s`
    el.style.animationDuration = `${duration}s`
    
    // Random position
    el.style.left = `${10 + Math.random() * 80}%`
    el.style.top = `${Math.random() * 100}%`
  })
}

function animateTechWaves() {
  const waves = document.querySelector('.tech-waves')
  if (waves) {
    // Animation logic for waves
    setInterval(() => {
      const wave = document.createElement('div')
      wave.classList.add('wave')
      if (!theme.global.current.value.dark) {
        wave.classList.add('light-mode')
      }
      waves.appendChild(wave)
      
      setTimeout(() => {
        if (waves.contains(wave)) {
          waves.removeChild(wave)
        }
      }, 3000)
    }, 2000)
  }
}
</script>

<style scoped>
/* Base styles */
.main-content {
  padding-top: 64px; /* This matches the height of your app bar */
}

body {
  cursor: none;
}
.custom-cursor {
  position: fixed;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: 1px solid rgba(255, 255, 255, 0.2);
  pointer-events: none;
  transform: translate(-50%, -50%);
  z-index: 9999;
}
.custom-cursor.light-mode {
  border: 1px solid rgba(0, 0, 0, 0.2);
}
.cursor-dot {
  position: fixed;
  width: 4px;
  height: 4px;
  background: white;
  border-radius: 50%;
  pointer-events: none;
  transform: translate(-50%, -50%);
  z-index: 9999;
}
.cursor-dot.light-mode {
  background: #121212;
}

/* Enhanced Service Cards */
.service-card {
  border-radius: 12px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  position: relative;
  overflow: hidden;
  backdrop-filter: blur(5px);
  border: 1px solid rgba(255, 255, 255, 0.1);
}
.service-card.light-mode {
  border: 1px solid rgba(0, 0, 0, 0.1);
}
.service-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
}
.service-card.light-mode:hover {
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}
.service-card::before {
  content: '';
  position: absolute;
  top: -100%;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, transparent 0%, rgba(255, 255, 255, 0.03) 50%, transparent 100%);
  transition: all 0.6s ease;
}
.service-card.light-mode::before {
  background: linear-gradient(135deg, transparent 0%, rgba(0, 0, 0, 0.03) 50%, transparent 100%);
}
.service-card:hover::before {
  top: 100%;
  left: 100%;
}

/* Abstract Tech Patterns */
.tech-pattern {
  position: fixed;
  opacity: 0.03;
  pointer-events: none;
  z-index: -1;
}
.tech-pattern.light-mode {
  opacity: 0.05;
}
.tech-pattern-1 {
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: radial-gradient(circle at 10% 20%, rgba(255, 255, 255, 0.1) 1px, transparent 1px);
  background-size: 30px 30px;
}
.tech-pattern-1.light-mode {
  background-image: radial-gradient(circle at 10% 20%, rgba(0, 0, 0, 0.1) 1px, transparent 1px);
}
.tech-pattern-2 {
  top: 10%;
  right: 5%;
  width: 300px;
  height: 300px;
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.05) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.05) 50%, rgba(255, 255, 255, 0.05) 75%, transparent 75%);
  background-size: 10px 10px;
  transform: rotate(15deg);
}
.tech-pattern-2.light-mode {
  background-image: linear-gradient(45deg, rgba(0, 0, 0, 0.05) 25%, transparent 25%, transparent 50%, rgba(0, 0, 0, 0.05) 50%, rgba(0, 0, 0, 0.05) 75%, transparent 75%);
}
.tech-pattern-3 {
  bottom: 15%;
  left: 10%;
  width: 200px;
  height: 200px;
  background-image: repeating-linear-gradient(0deg, rgba(255, 255, 255, 0.03), rgba(255, 255, 255, 0.03) 1px, transparent 1px, transparent 5px);
  transform: rotate(-20deg);
}
.tech-pattern-3.light-mode {
  background-image: repeating-linear-gradient(0deg, rgba(0, 0, 0, 0.03), rgba(0, 0, 0, 0.03) 1px, transparent 1px, transparent 5px);
}

/* Tech Grid */
.tech-grid {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
                    linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
  background-size: 50px 50px;
  opacity: 0.4;
  pointer-events: none;
  z-index: -1;
}
.tech-grid.light-mode {
  background-image: linear-gradient(rgba(0, 0, 0, 0.02) 1px, transparent 1px),
                    linear-gradient(90deg, rgba(0, 0, 0, 0.02) 1px, transparent 1px);
}

/* Circuit Lines for Hero Section */
.circuit-lines {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: 
    radial-gradient(circle at 20% 35%, rgba(100, 255, 218, 0.1) 0%, transparent 25%),
    radial-gradient(circle at 75% 44%, rgba(100, 218, 255, 0.1) 0%, transparent 25%);
  opacity: 0.5;
  pointer-events: none;
}
.circuit-lines.light-mode {
  background-image: 
    radial-gradient(circle at 20% 35%, rgba(0, 150, 136, 0.08) 0%, transparent 25%),
    radial-gradient(circle at 75% 44%, rgba(33, 150, 243, 0.08) 0%, transparent 25%);
}

/* Glitch Text Effect */
.glitch-text {
  position: relative;
  text-shadow: 0 0 1px rgba(255, 255, 255, 0.3);
}
.light-mode .glitch-text {
  text-shadow: 0 0 1px rgba(0, 0, 0, 0.3);
}
.glitch-text::before,
.glitch-text::after {
  content: 'Innovate. Launch. Scale.';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  pointer-events: none;
}
.glitch-text::before {
  left: 2px;
  text-shadow: 0 0 3px rgba(100, 255, 255, 0.6);
  animation: glitch-effect 3s infinite alternate-reverse;
}
.light-mode .glitch-text::before {
  text-shadow: 0 0 3px rgba(0, 150, 255, 0.6);
}
.glitch-text::after {
  left: -2px;
  text-shadow: 0 0 3px rgba(255, 100, 255, 0.6);
  animation: glitch-effect 2s infinite alternate-reverse;
}
.light-mode .glitch-text::after {
  text-shadow: 0 0 3px rgba(150, 0, 150, 0.6);
}
@keyframes glitch-effect {
  0%, 95% { opacity: 0; }
  96%, 100% { opacity: 0.2; }
}

/* Enhanced Tech Button */
.tech-btn {
  position: relative;
  overflow: hidden;
  transition: all 0.3s ease;
  border: 1px solid rgba(255, 255, 255, 0.2);
}
.light-mode .tech-btn {
  border: 1px solid rgba(0, 0, 0, 0.2);
}
.tech-btn .btn-hover-effect {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
  transition: left 0.5s ease;
}
.light-mode .tech-btn .btn-hover-effect {
  background: linear-gradient(90deg, transparent, rgba(0, 0, 0, 0.05), transparent);
}
.tech-btn:hover .btn-hover-effect {
  left: 100%;
}
.tech-btn:hover {
  box-shadow: 0 0 15px rgba(255, 255, 255, 0.2);
}
.light-mode .tech-btn:hover {
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
}

/* Floating Tech Elements */
.floating-tech-elements {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}
.tech-element {
  position: absolute;
  width: 30px;
  height: 30px;
  background-color: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 30%;
  transform: rotate(45deg);
  animation: float-vertical ease-in-out infinite alternate;
  z-index: 1;
}
.tech-element.light-mode {
  background-color: rgba(0, 0, 0, 0.03);
  border: 1px solid rgba(0, 0, 0, 0.05);
}
.tech-element::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 60%;
  height: 60%;
  transform: translate(-50%, -50%);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 30%;
}
.tech-element.light-mode::before {
  border: 1px solid rgba(0, 0, 0, 0.1);
}
@keyframes float-vertical {
  0% { transform: rotate(45deg) translateY(0); }
  100% { transform: rotate(45deg) translateY(20px); }
}

/* Tech Dots Background */
.tech-dots {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: radial-gradient(rgba(255, 255, 255, 0.1) 1px, transparent 1px);
  background-size: 20px 20px;
  opacity: 0.5;
  pointer-events: none;
}
.tech-dots.light-mode {
  background-image: radial-gradient(rgba(0, 0, 0, 0.1) 1px, transparent 1px);
}

/* Service Card Enhancements */
.service-icon-wrapper {
  position: relative;
  display: inline-block;
}
.service-icon {
  position: relative;
  z-index: 2;
}
.icon-ripple {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.03);
  z-index: 1;
}
.icon-ripple.light-mode {
  background: rgba(0, 0, 0, 0.03);
}
.service-card:hover .icon-ripple {
  animation: ripple 1.5s ease-out infinite;
}
@keyframes ripple {
  0% {
    transform: translate(-50%, -50%) scale(0.8);
    opacity: 1;
  }
  100% {
    transform: translate(-50%, -50%) scale(1.5);
    opacity: 0;
  }
}
.card-corner-accent {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 30px;
  height: 30px;
  overflow: hidden;
}
.card-corner-accent::before {
  content: '';
  position: absolute;
  bottom: 0;
  right: 0;
  width: 200%;
  height: 200%;
  background: linear-gradient(135deg, transparent 50%, rgba(255, 255, 255, 0.1) 51%);
}
.card-corner-accent.light-mode::before {
  background: linear-gradient(135deg, transparent 50%, rgba(0, 0, 0, 0.05) 51%);
}

/* Tech Waves for CTA Section */
.tech-waves {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  pointer-events: none;
}
.wave {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: 1px solid rgba(255, 255, 255, 0.1);
  animation: wave-expand 3s ease-out forwards;
}
.wave.light-mode {
  border: 1px solid rgba(0, 0, 0, 0.1);
}
@keyframes wave-expand {
  0% {
    width: 20px;
    height: 20px;
    opacity: 0.5;
  }
  100% {
    width: 500px;
    height: 500px;
    opacity: 0;
  }
}

/* Tech Contact Button */
.tech-contact-btn {
  position: relative;
  overflow: hidden;
}
.btn-pulse {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
  height: 100%;
  background: radial-gradient(circle, rgba(255, 255, 255, 0.2) 0%, transparent 70%);
  opacity: 0;
}
.btn-pulse.light-mode {
  background: radial-gradient(circle, rgba(0, 0, 0, 0.1) 0%, transparent 70%);
}
.tech-contact-btn:hover .btn-pulse {
  animation: pulse 1.5s ease-out infinite;
}
@keyframes pulse {
  0% {
    transform: translate(-50%, -50%) scale(0.8);
    opacity: 0.5;
  }
  100% {
    transform: translate(-50%, -50%) scale(1.5);
    opacity: 0;
  }
}

/* For mobile devices */
@media (max-width: 600px) {
  .main-content {
    padding-top: 56px; /* Smaller padding for mobile */
  }
}
</style>