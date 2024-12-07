<script setup lang="ts">
defineProps(["elements"]);

export interface SidebarElement {
  icon: string;
  text: string;
}
</script>

<template>
  <div class="sidebar-and-outline">
    <div class="sidebar">
      <div class="sidebar-element" v-for="e in elements">
        <span :class="`icon fa-solid fa-${e.icon}`" aria-hidden="true" />
        <span class="sidebar-element-text">{{ e.text }}</span>
      </div>
    </div>
    <div class="sidebar-outline"></div>
  </div>
</template>

<style scoped>
@import "./theme.css";

.sidebar-and-outline {
  display: flex;
}

.sidebar {
  display: flex;
  flex-direction: column;
  font-size: var(--navigation-font-size);
  min-width: 160pt;
}

.sidebar-outline {
  height: 100vh;
  margin-top: calc(-1 * var(--page-padding)); /** Hack! Haaaack! */
  margin-left: 5px;
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

@media screen and (max-width: 1000px) {
  .sidebar {
    flex-direction: row;
    position: fixed;
    font-size: 14pt;

    border-style: none;
  }

  .sidebar-outline {
    display: none;
  }

  .icon {
    margin: 0;
  }

  .sidebar-element-text {
    display: none;
  }
}
</style>
