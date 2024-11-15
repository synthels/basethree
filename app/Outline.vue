<script setup lang="ts">
import User from "./components/User.vue";
import Sidebar, { SidebarElement } from "./components/Sidebar.vue";

const sidebar: SidebarElement[] = [
  {
    icon: "house",
    text: "Home",
  },
  {
    icon: "trophy",
    text: "Leaderboard",
  },
  {
    icon: "gear",
    text: "Settings",
  },
];
</script>

<template>
  <div class="outline">
    <User />
    <Sidebar :elements="sidebar" />
  </div>
</template>

<style scoped>
@import "./components/theme.css";

.outline {
  padding: var(--page-padding);
}

@media screen and (max-width: 700px) {
  .outline {
  }
}
</style>
