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
  <div class="home">
    <User />
    <Sidebar :elements="sidebar" />
  </div>
</template>

<style scoped>
@import "./components/theme.css";

.home {
  padding: var(--page-padding);
}
</style>
