
<template>
    <!-- Header -->
    <AppHeader :menu-items="menuItems" @navigate="handleNavigation" />
    <v-app>
      <!-- Custom Cursor -->
      <div class="custom-cursor" :class="{ 'light-mode': !isDarkTheme }" ref="customCursor"></div>
      <div class="cursor-dot" :class="{ 'light-mode': !isDarkTheme }" ref="cursorDot"></div>
  
      <!-- Abstract Tech Backgrounds -->
      <div class="tech-pattern tech-pattern-1" :class="{ 'light-mode': !isDarkTheme }"></div>
      <div class="tech-pattern tech-pattern-2" :class="{ 'light-mode': !isDarkTheme }"></div>
      <div class="tech-pattern tech-pattern-3" :class="{ 'light-mode': !isDarkTheme }"></div>
      <div class="tech-grid" :class="{ 'light-mode': !isDarkTheme }"></div>
  
      
  
      <v-main>
        <v-container class="contact-page py-16 mt-10 position-relative">
          <!-- Abstract Tech Patterns -->
          <div class="tech-pattern tech-pattern-1" :class="{ 'light-mode': !isDarkTheme }"></div>
          <div class="tech-pattern tech-pattern-2" :class="{ 'light-mode': !isDarkTheme }"></div>
          <div class="circuit-board-bg" :class="{ 'light-mode': !isDarkTheme }"></div>
          <div class="tech-dots" :class="{ 'light-mode': !isDarkTheme }"></div>
      
          <!-- Section Title -->
          <v-row justify="center" class="mb-12">
            <v-col cols="12" class="text-center">
              <h1 class="text-h4 font-weight-light">Contact <span class="tech-gradient-text">Us</span></h1>
              <div class="title-underline mx-auto mt-2"></div>
              <p class="text-body-1 text-medium-emphasis mt-4 max-width-500 mx-auto">
                Have a project in mind? We're ready to turn your ideas into reality. 
                Reach out and let's start the conversation.
              </p>
            </v-col>
          </v-row>
  
          <v-row>
            <!-- Contact Form -->
            <v-col cols="12" md="6">
              <v-card 
                class="contact-card pa-6" 
                :class="{ 'light-mode': !isDarkTheme }" 
                variant="flat"
                :style="{
                  backgroundColor: isDarkTheme ? 'rgba(30, 30, 30, 0.7)' : 'rgba(255, 255, 255, 0.7)'
                }"
              >
                <div class="card-corner-accent" :class="{ 'light-mode': !isDarkTheme }"></div>
                <v-form ref="form" v-model="valid" lazy-validation>
                  <v-row>
                    <v-col cols="12" sm="6">
                      <v-text-field
                        v-model="name"
                        :rules="nameRules"
                        label="Name"
                        variant="outlined"
                        required
                        class="tech-input"
                        :class="{ 'light-mode': !isDarkTheme }"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6">
                      <v-text-field
                        v-model="email"
                        :rules="emailRules"
                        label="Email"
                        variant="outlined"
                        required
                        class="tech-input"
                        :class="{ 'light-mode': !isDarkTheme }"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12">
                      <v-text-field
                        v-model="subject"
                        label="Subject"
                        variant="outlined"
                        class="tech-input"
                        :class="{ 'light-mode': !isDarkTheme }"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12">
                      <v-textarea
                        v-model="message"
                        :rules="messageRules"
                        label="Message"
                        variant="outlined"
                        required
                        rows="6"
                        class="tech-input"
                        :class="{ 'light-mode': !isDarkTheme }"
                      ></v-textarea>
                    </v-col>
                    <v-col cols="12" class="d-flex justify-end">
                      <v-btn 
                        variant="flat" 
                        size="large" 
                        color="primary" 
                        class="tech-submit-btn"
                        :class="{ 'light-mode': !isDarkTheme }"
                        @click="submitForm"
                        :loading="loading"
                      >
                        <span class="btn-text">Send Message</span>
                        <span class="btn-hover-effect"></span>
                      </v-btn>
                    </v-col>
                  </v-row>
                </v-form>
              </v-card>
            </v-col>
  
            <!-- Contact Info -->
            <v-col cols="12" md="6">
              <div class="info-container h-100 d-flex flex-column">
                <v-card 
                  class="info-card mb-4 pa-5" 
                  :class="{ 'light-mode': !isDarkTheme }" 
                  variant="flat"
                  :style="{
                    backgroundColor: isDarkTheme ? 'rgba(30, 30, 30, 0.7)' : 'rgba(255, 255, 255, 0.7)'
                  }"
                >
                  <div class="d-flex align-center">
                    <div class="info-icon-wrapper mr-4" :class="{ 'light-mode': !isDarkTheme }">
                      <v-icon size="28" :color="isDarkTheme ? 'white' : 'primary'">mdi-map-marker</v-icon>
                      <div class="icon-glow" :class="{ 'light-mode': !isDarkTheme }"></div>
                    </div>
                    <div>
                      <h3 class="text-h6 font-weight-medium mb-1">Our Location</h3>
                      <p class="text-body-2 text-medium-emphasis mb-0">
                        L. De Leon St.<br>
                        Taguig City, Metro Manila
                      </p>
                    </div>
                  </div>
                </v-card>
  
                <v-card 
                  class="info-card mb-4 pa-5" 
                  :class="{ 'light-mode': !isDarkTheme }" 
                  variant="flat"
                  :style="{
                    backgroundColor: isDarkTheme ? 'rgba(30, 30, 30, 0.7)' : 'rgba(255, 255, 255, 0.7)'
                  }"
                >
                  <div class="d-flex align-center">
                    <div class="info-icon-wrapper mr-4" :class="{ 'light-mode': !isDarkTheme }">
                      <v-icon size="28" :color="isDarkTheme ? 'white' : 'primary'">mdi-phone</v-icon>
                      <div class="icon-glow" :class="{ 'light-mode': !isDarkTheme }"></div>
                    </div>
                    <div>
                      <h3 class="text-h6 font-weight-medium mb-1">Call Us</h3>
                      <p class="text-body-2 text-medium-emphasis mb-0">
                        +63 966 593 2267<br>
                        Monday-Friday, 9am-6pm PHT
                      </p>
                    </div>
                  </div>
                </v-card>
  
                <v-card 
                  class="info-card mb-4 pa-5" 
                  :class="{ 'light-mode': !isDarkTheme }" 
                  variant="flat"
                  :style="{
                    backgroundColor: isDarkTheme ? 'rgba(30, 30, 30, 0.7)' : 'rgba(255, 255, 255, 0.7)'
                  }"
                >
                  <div class="d-flex align-center">
                    <div class="info-icon-wrapper mr-4" :class="{ 'light-mode': !isDarkTheme }">
                      <v-icon size="28" :color="isDarkTheme ? 'white' : 'primary'">mdi-email</v-icon>
                      <div class="icon-glow" :class="{ 'light-mode': !isDarkTheme }"></div>
                    </div>
                    <div>
                      <h3 class="text-h6 font-weight-medium mb-1">Email Us</h3>
                      <p class="text-body-2 text-medium-emphasis mb-0">
                        info@linkerx.com<br>
                        support@linkerx.com
                      </p>
                    </div>
                  </div>
                </v-card>
  
                <!-- Social Media -->
                <v-card 
                  class="info-card social-card mt-auto pa-5" 
                  :class="{ 'light-mode': !isDarkTheme }" 
                  variant="flat"
                  :style="{
                    backgroundColor: isDarkTheme ? 'rgba(30, 30, 30, 0.7)' : 'rgba(255, 255, 255, 0.7)'
                  }"
                >
                  <h3 class="text-h6 font-weight-medium mb-3">Connect With Us</h3>
                  <div class="d-flex">
                    <v-btn icon class="social-icon mr-2" :class="{ 'light-mode': !isDarkTheme }" variant="plain"
                    href="https://www.facebook.com/linkerx.dev/" target="_blank">
                      <v-icon :color="isDarkTheme ? 'white' : 'primary'">mdi-facebook</v-icon>
                      <div class="social-hover-effect" :class="{ 'light-mode': !isDarkTheme }"></div>
                    </v-btn>
                    <v-btn icon class="social-icon mr-2" :class="{ 'light-mode': !isDarkTheme }" variant="plain" 
                    href="https://www.linkedin.com/company/linker-x/" target="_blank">
                      <v-icon :color="isDarkTheme ? 'white' : 'primary'">mdi-linkedin</v-icon>
                      <div class="social-hover-effect" :class="{ 'light-mode': !isDarkTheme }"></div>
                    </v-btn>
                  </div>
                </v-card>
              </div>
            </v-col>
          </v-row>
  
          <!-- Map Section -->
        <v-row class="mt-12">
        <v-col cols="12">
            <div class="map-container position-relative">
            <!-- Google Maps iframe -->
            <div class="iframe-wrapper">
              <iframe src="https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d1623.970535230273!2d121.07089641111223!3d14.51482237771015!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m2!1m1!2s!5e0!3m2!1sen!2sph!4v1751992172662!5m2!1sen!2sph" width="100%" 
                height="400" style="border:0; border-radius: 12px; filter: invert(90%);"  allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>                
            </div>
            <div class="map-overlay" :class="{ 'light-mode': !isDarkTheme }"></div>
            
            <div class="tech-frame" :class="{ 'light-mode': !isDarkTheme }"></div>
            </div>
        </v-col>
        </v-row>
        
          <!-- Notification -->
          <v-snackbar
            v-model="snackbar"
            :timeout="4000"
            :color="snackbarColor"
            location="top"
          >
            {{ snackbarText }}
            <template v-slot:actions>
              <v-btn
                variant="text"
                @click="snackbar = false"
              >
                Close
              </v-btn>
            </template>
          </v-snackbar>
        </v-container>
      </v-main>
    </v-app>
  </template>
  
  <script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { useTheme } from 'vuetify'
import { useRouter } from 'vue-router'
import axios from 'axios'
import AppHeader from '@/components/AppHeader.vue'
import AppFooter from '@/components/AppFooter.vue'

const theme = useTheme()
const router = useRouter()
const customCursor = ref(null)
const cursorDot = ref(null)

// Check if theme is dark mode
const isDarkTheme = computed(() => theme.global.current.value.dark)

const menuItems = [
  { title: 'Home', target: 'home' },
  { title: 'Services', target: 'services' },
  { title: 'About', target: 'about' }
]

const handleNavigation = (id) => {
  if (id === 'home') {
    router.push('/')
  } else {
    const el = document.getElementById(id)
    if (el) el.scrollIntoView({ behavior: 'smooth' })
  }
}

// Cursor logic
onMounted(() => {
  window.addEventListener('mousemove', updateCursor)
  document.addEventListener('mousedown', expandCursor)
  document.addEventListener('mouseup', shrinkCursor)
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
    customCursor.value.style.backgroundColor = isDarkTheme.value
      ? 'rgba(255, 255, 255, 0.05)'
      : 'rgba(0, 0, 0, 0.05)'
  }
}

function shrinkCursor() {
  if (customCursor.value) {
    customCursor.value.style.width = '20px'
    customCursor.value.style.height = '20px'
    customCursor.value.style.backgroundColor = 'transparent'
  }
}

// Form validation
const valid = ref(false)
const name = ref('')
const email = ref('')
const subject = ref('')
const message = ref('')
const loading = ref(false)
const form = ref(null)

// Snackbar
const snackbar = ref(false)
const snackbarText = ref('')
const snackbarColor = ref('success')

// Validation rules
const nameRules = [
  v => !!v || 'Name is required',
  v => v.length <= 50 || 'Name must be less than 50 characters'
]

const emailRules = [
  v => !!v || 'Email is required',
  v => /.+@.+\..+/.test(v) || 'Email must be valid'
]

const messageRules = [
  v => !!v || 'Message is required',
  v => v.length >= 10 || 'Message must be at least 10 characters'
]

// Form submission using axios
const submitForm = async () => {
  const isValid = await form.value.validate()

  if (isValid.valid) {
    loading.value = true

    try {
      await axios.post(' https://linkerx.dev/send-email', {
        name: name.value,
        email: email.value,
        subject: subject.value,
        message: message.value
      })

      snackbarText.value = 'Your message has been sent successfully!'
      snackbarColor.value = 'success'
      snackbar.value = true

      form.value.reset()
    } catch (error) {
      console.error('Failed to send:', error)
      snackbarText.value = 'Failed to send message. Please try again later.'
      snackbarColor.value = 'error'
      snackbar.value = true
    } finally {
      loading.value = false
    }
  } else {
    snackbarText.value = 'Please fill out all required fields correctly.'
    snackbarColor.value = 'error'
    snackbar.value = true
  }
}
</script>

  
  <style scoped>
  /* Base Cursor Styles */
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

  /* Iframe Wrapper Styles */
.iframe-wrapper {
  position: relative;
  z-index: 1;
  border-radius: 12px;
  overflow: hidden;
}

/* Additional Map Styles */
.map-overlay {
  pointer-events: none; /* Allow clicking through to the map */
}
  
  /* Abstract Tech Patterns */
  .tech-pattern-3 {
    bottom: 15%;
    left: 10%;
    width: 200px;
    height: 200px;
    background-image: repeating-linear-gradient(0deg, rgba(255, 255, 255, 0.03), rgba(255, 255, 255, 0.03) 1px, transparent 1px, transparent 5px);
    transform: rotate(-20deg);
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
  
  /* Tech Patterns */
  .tech-pattern {
    position: absolute;
    opacity: 0.05;
    pointer-events: none;
    z-index: -1;
  }
  .tech-pattern-1 {
    top: 5%;
    right: 0;
    width: 300px;
    height: 300px;
    background-image: radial-gradient(circle at 30% 70%, rgba(255, 255, 255, 0.1) 1px, transparent 1px);
    background-size: 20px 20px;
  }
  .tech-pattern-2 {
    bottom: 10%;
    left: 5%;
    width: 200px;
    height: 200px;
    background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.05) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.05) 50%, rgba(255, 255, 255, 0.05) 75%, transparent 75%);
    background-size: 10px 10px;
    transform: rotate(15deg);
  }
  
  /* Circuit Board Background */
  .circuit-board-bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: 
      linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
      linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
      radial-gradient(circle at 75% 25%, rgba(100, 200, 255, 0.05) 0%, transparent 40%);
    background-size: 20px 20px;
    opacity: 0.4;
    pointer-events: none;
    z-index: -1;
  }
  
  /* Tech Dots */
  .tech-dots {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: radial-gradient(rgba(255, 255, 255, 0.1) 1px, transparent 1px);
    background-size: 20px 20px;
    opacity: 0.3;
    pointer-events: none;
    z-index: -1;
  }
  
  /* Section Title Styles */
  .tech-gradient-text {
    background: linear-gradient(90deg, #64c8ff, #64ffd8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent;
  }
  .title-underline {
    width: 80px;
    height: 3px;
    background: linear-gradient(90deg, #64c8ff, #64ffd8);
    border-radius: 3px;
  }
  .max-width-500 {
    max-width: 500px;
  }
  
  /* Contact Card Styles */
  /* Updated Contact Card Styles */
.contact-card, .info-card {
  border-radius: 12px;
  overflow: hidden;
  backdrop-filter: blur(5px);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  position: relative;
}

/* Dark mode specific styles */
:deep(.theme--dark) .contact-card,
:deep(.theme--dark) .info-card,
.contact-card:not(.light-mode),
.info-card:not(.light-mode) {
  border: 1px solid rgba(255, 255, 255, 0.1);
  background-color: rgba(30, 30, 30, 0.7) !important;
}

/* Light mode specific styles */
:deep(.theme--light) .contact-card,
:deep(.theme--light) .info-card,
.contact-card.light-mode,
.info-card.light-mode {
  border: 1px solid rgba(0, 0, 0, 0.1);
  background-color: rgba(255, 255, 255, 0.7) !important;
}

.contact-card:hover, .info-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
}

/* Form Input Styling - Dark Mode */
:deep(.theme--dark) .tech-input .v-field__outline,
.tech-input:not(.light-mode) :deep(.v-field__outline) {
  border-color: rgba(255, 255, 255, 0.1) !important;
}

:deep(.theme--dark) .tech-input .v-field--focused .v-field__outline,
.tech-input:not(.light-mode) :deep(.v-field--focused .v-field__outline) {
  border-color: rgba(100, 200, 255, 0.5) !important;
}

:deep(.theme--dark) .tech-input .v-field:hover .v-field__outline,
.tech-input:not(.light-mode) :deep(.v-field:hover .v-field__outline) {
  border-color: rgba(255, 255, 255, 0.2) !important;
}

/* Form Input Styling - Light Mode */
:deep(.theme--light) .tech-input .v-field__outline,
.tech-input.light-mode :deep(.v-field__outline) {
  border-color: rgba(0, 0, 0, 0.1) !important;
}

:deep(.theme--light) .tech-input .v-field--focused .v-field__outline,
.tech-input.light-mode :deep(.v-field--focused .v-field__outline) {
  border-color: rgba(33, 150, 243, 0.5) !important;
}

:deep(.theme--light) .tech-input .v-field:hover .v-field__outline,
.tech-input.light-mode :deep(.v-field:hover .v-field__outline) {
  border-color: rgba(0, 0, 0, 0.2) !important;
}

/* Submit Button - Dark Mode */
:deep(.theme--dark) .tech-submit-btn,
.tech-submit-btn:not(.light-mode) {
  background: linear-gradient(135deg, #64c8ff, #64ffd8) !important;
  color: #121212 !important;
}

/* Submit Button - Light Mode */
:deep(.theme--light) .tech-submit-btn,
.tech-submit-btn.light-mode {
  background: linear-gradient(135deg, #1976d2, #0d47a1) !important;
  color: white !important;
}
  
  /* Info Cards */
  .info-container {
    height: 100%;
  }
  .info-card {
    transition: all 0.3s ease;
  }
  .info-icon-wrapper {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background-color: rgba(100, 200, 255, 0.1);
  }
  .icon-glow {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: rgba(100, 200, 255, 0.3);
    opacity: 0;
    transition: opacity 0.3s ease, transform 0.3s ease;
    transform: scale(0.8);
  }
  .info-card:hover .icon-glow {
    opacity: 0.3;
    transform: scale(1.1);
  }
  
  /* Social Icons */
  .social-icon {
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
    margin-right: 8px;
  }
  .social-hover-effect {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle, rgba(100, 200, 255, 0.2) 0%, transparent 70%);
    opacity: 0;
    transition: opacity 0.3s ease;
    border-radius: 50%;
  }
  .social-icon:hover .social-hover-effect {
    opacity: 1;
  }
  
  /* Map Container */
  .map-container {
    margin-top: 30px;
    border-radius: 12px;
    overflow: hidden;
  }
  .map-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, rgba(100, 200, 255, 0.1), transparent);
    pointer-events: none;
    z-index: 2;
  }
  .map-marker {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 3;
  }
  .marker-pulse {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: rgba(244, 67, 54, 0.2);
    animation: pulse 2s infinite;
    z-index: 1;
  }
  @keyframes pulse {
    0% {
      transform: translate(-50%, -50%) scale(0.5);
      opacity: 1;
    }
    100% {
      transform: translate(-50%, -50%) scale(1.5);
      opacity: 0;
    }
  }
  .tech-frame {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    pointer-events: none;
    z-index: 4;
  }
  .tech-frame::before,
  .tech-frame::after {
    content: '';
    position: absolute;
    width: 30px;
    height: 30px;
    border: 1px solid rgba(255, 255, 255, 0.3);
  }
  .tech-frame::before {
    top: -1px;
    left: -1px;
    border-right: none;
    border-bottom: none;
  }
  .tech-frame::after {
    bottom: -1px;
    right: -1px;
    border-left: none;
    border-top: none;
  }
  </style>