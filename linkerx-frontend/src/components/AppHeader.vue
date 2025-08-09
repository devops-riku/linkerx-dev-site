<!-- AppHeader.vue -->
<template>
  <header class="app-header" :style="headerStyle">
    <div class="header-container">
      <h2 class="font-weight-medium mb-0">{{ title }}</h2>

      <div class="d-none d-md-flex align-center">
        <button
          v-for="item in filteredMenuItems"
          :key="item.title" 
          class="nav-btn hover-effect text-body-2 mx-2"
          @click="$emit('navigate', item.target)"
        >
          {{ item.title }}
        </button>
        <button
          v-if="!isContactPage"
          class="contact-btn hover-effect"
          @click="$emit('navigate', 'contact')"
        >
          Contact
        </button>
      </div>

      <!-- Mobile Burger -->
      <button class="mobile-menu-btn d-flex d-md-none" @click="mobileMenu = true">
        <span class="menu-icon"></span>
      </button>

      <!-- Mobile Menu Dialog -->
      <div v-if="mobileMenu" class="mobile-menu-overlay">
        <div class="mobile-menu" :style="mobileMenuStyle">
          <div class="mobile-header">
            <span>{{ title }}</span>
            <button class="close-btn" @click="mobileMenu = false">×</button>
          </div>
          <div class="menu-divider"></div>
          <div class="mobile-menu-items">
            <div
              v-for="item in filteredMenuItems"
              :key="item.title"
              class="mobile-menu-item"
              @click="handleNav(item.target)"
            >
              {{ item.title }}
            </div>
            <div 
              v-if="!isContactPage"
              class="mobile-menu-item" 
              @click="handleNav('contact')"
            >
              Contact
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { ref, computed } from 'vue'
import { useTheme } from 'vuetify'

const route = useRoute()
const theme = useTheme()

// Computed styles based on the current theme
const headerStyle = computed(() => {
  const isDark = theme.global.current.value.dark
  return {
    backgroundColor: isDark ? '#121212' : 'white',
    color: isDark ? 'white' : '#121212',
    boxShadow: isDark ? '0 2px 4px rgba(0, 0, 0, 0.3)' : '0 2px 8px rgba(0, 0, 0, 0.1)'
  }
})

const mobileMenuStyle = computed(() => {
  const isDark = theme.global.current.value.dark
  return {
    backgroundColor: isDark ? '#121212' : 'white',
    color: isDark ? 'white' : '#121212'
  }
})

const isHome = computed(() => route.path === '/')
const isContactPage = computed(() => route.path === '/contact-us')

// Filter menu items based on the current route
const filteredMenuItems = computed(() => {
  if (isContactPage.value) {
    // Only show Home button on Contact page
    return props.menuItems.filter(item => item.target === 'home')
  } else {
    // Show all menu items on other pages
    return props.menuItems
  }
})

const props = defineProps({
  title: {
    type: String,
    default: 'Linkerx',
  },
  menuItems: {
    type: Array,
    default: () => [
      { title: 'Home', target: 'home' },
      { title: 'Services', target: 'services' },
      { title: 'About', target: 'about' },
    ],
  },
})

const mobileMenu = ref(false)

const emit = defineEmits(['navigate'])

const handleNav = (target) => {
  emit('navigate', target)
  mobileMenu.value = false
}
</script>

<style scoped>
.app-header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 64px;
  background-color: #121212;
  color: white;
  z-index: 999;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  transition: background-color 0.3s ease, color 0.3s ease;
}

.app-header.light-mode {
  background-color: white;
  color: #121212;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.header-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 16px;
  height: 100%;
  max-width: 1280px;
  margin: 0 auto;
}

.nav-btn {
  background: none;
  border: none;
  color: inherit;
  font-size: 14px;
  cursor: pointer;
  padding: 8px 12px;
}

.contact-btn {
  background: none;
  border: 1px solid currentColor;
  color: inherit;
  opacity: 0.8;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.contact-btn:hover {
  opacity: 1;
  transform: translateY(-2px);
}

.mobile-menu-btn {
  background: none;
  border: none;
  color: inherit;
  cursor: pointer;
}

.menu-icon {
  display: block;
  width: 24px;
  height: 2px;
  background-color: currentColor;
  position: relative;
}

.menu-icon::before,
.menu-icon::after {
  content: '';
  position: absolute;
  width: 24px;
  height: 2px;
  background-color: currentColor;
  left: 0;
}

.menu-icon::before {
  top: -6px;
}

.menu-icon::after {
  bottom: -6px;
}

.mobile-menu-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  z-index: 1000;
}

.mobile-menu {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #121212;
  color: white;
  z-index: 1001;
  padding: 16px;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.mobile-menu.light-mode {
  background-color: white;
  color: #121212;
}

.mobile-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.close-btn {
  background: none;
  border: none;
  color: inherit;
  font-size: 24px;
  cursor: pointer;
}

.menu-divider {
  height: 1px;
  background-color: currentColor;
  opacity: 0.1;
  margin: 16px 0;
}

.mobile-menu-items {
  padding: 16px 0;
}

.mobile-menu-item {
  padding: 12px 0;
  font-size: 16px;
  cursor: pointer;
}

.hover-effect {
  position: relative;
  transition: color 0.3s ease;
}

.hover-effect::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  height: 1px;
  width: 0;
  background-color: currentColor;
  transition: width 0.3s;
}

.hover-effect:hover::after {
  width: 100%;
}

/* For mobile devices */
@media (max-width: 600px) {
  .app-header {
    height: 56px;
  }
}
</style>