<script setup lang="ts">
defineProps(["elements"]);

export interface SidebarElement {
  icon: string;
  text: string;
}
</script>

<template>
  <div class="sidebar">
    <div class="sidebar-element" v-for="e in elements">
      <span :class="`fa-solid fa-${e.icon}`" aria-hidden="true" />
      <span class="margin-right" />
      {{ e.text }}
    </div>
  </div>
</template>

<style scoped>
.sidebar {
  display: flex;
  flex-direction: column;
  float: left;
  font-size: var(--navigation-font-size);
  width: 240pt;
}

.sidebar-element {
  color: var(--text);
  padding: var(--element-padding);
  border-radius: var(--border-radius);
}

.sidebar-element:hover {
  background-color: var(--secondary);
  cursor: pointer;
}
</style>
