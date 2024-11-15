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
      <span :class="`icon fa-solid fa-${e.icon}`" aria-hidden="true" />
      <span class="sidebar-element-text">{{ e.text }}</span>
    </div>
  </div>
</template>

<style scoped>
.sidebar {
  display: flex;
  flex-direction: column;
  float: left;
  font-size: var(--navigation-font-size);
  min-width: 160pt;

  border-color: var(--secondary);
  border-right-style: solid;
  border-right-width: 1px;
}

.sidebar-element {
  color: var(--text);
  padding: var(--element-padding);
  border-radius: var(--border-radius);
}

.icon {
  margin-right: 8px;
}

.sidebar-element:hover {
  background-color: var(--secondary);
  cursor: pointer;
}

@media screen and (max-width: 700px) {
  .sidebar {
    flex-direction: row;
    position: fixed;
    font-size: 14pt;

    border-style: none;
  }

  .icon {
    margin: 0;
  }

  .sidebar-element-text {
    display: none;
  }
}
</style>
