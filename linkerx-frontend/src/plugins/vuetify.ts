// plugins/vuetify.ts

import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

import { createVuetify } from 'vuetify'
import { md3 } from 'vuetify/blueprints'
import { aliases, mdi } from 'vuetify/iconsets/mdi'

// Custom Themes
const customDarkTheme = {
  dark: true,
  colors: {
    background: '#000000',
    surface: '#121212',
    primary: '#ffffff',
    secondary: '#1e88e5',
    error: '#ef5350',
    info: '#2196f3',
    success: '#4caf50',
    warning: '#ff9800',
    'on-surface': '#ffffff',
    'on-primary': '#ffffff'
  }
}

const customLightTheme = {
  dark: false,
  colors: {
    background: '#ffffff',
    surface: '#f5f5f5',
    primary: '#1976d2',
    secondary: '#424242',
    error: '#e53935',
    info: '#2196f3',
    success: '#43a047',
    warning: '#fb8c00',
    'on-surface': '#000000',
    'on-primary': '#ffffff'
  }
}

// Create Vuetify instance
const vuetify = createVuetify({
  blueprint: md3,
  theme: {
    defaultTheme: 'dark', // You can change to 'light' or dynamically set later
    themes: {
      dark: customDarkTheme,
      light: customLightTheme
    }
  },
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi
    }
  }
})

export default vuetify
