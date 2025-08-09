<template>
  <v-footer 
    app 
    height="48" 
    class="px-4" 
    :style="{
      backgroundColor: theme.global.current.value.dark ? '#000000' : theme.global.current.value.colors.surface,
      color: theme.global.current.value.dark ? 'white' : theme.global.current.value.colors['on-surface']
    }"
  >
    <v-container class="d-flex justify-between align-center flex-wrap text-caption">
      <!-- Left: Copyright -->
      <div>
        &copy;{{ new Date().getFullYear() }} Linkerx — All rights reserved.
      </div>

      <!-- Right: Social Icons -->
      <div class="d-flex align-center flex-wrap">
        <a
          v-for="item in items"
          :key="item.title"
          class="d-inline-flex align-center mx-2 social-link"
          :href="item.href"
          rel="noopener noreferrer"
          target="_blank"
          :title="item.title"
        >
          <v-icon :icon="item.icon" size="18" :color="iconColor" />
        </a>
      </div>
    </v-container>
  </v-footer>
</template>

<script setup lang="ts">
import { useTheme } from 'vuetify'
import { computed } from 'vue'

const theme = useTheme()

// Computed property for icon color based on current theme
const iconColor = computed(() => {
  return theme.global.current.value.dark ? 'white' : theme.global.current.value.colors.primary
})

defineProps<{
  items?: {
    title: string
    icon: string
    href: string
  }[]
}>()
</script>

<style scoped lang="scss">
.social-link :deep(.v-icon) {
  transition: 0.2s ease-in-out;

  &:hover {
    color: #77b5fe !important; // Use !important to override Vuetify's color property
    transform: translateY(-2px);
  }
}
</style>