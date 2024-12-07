<script setup lang="ts">
import User from "./components/User.vue";
import Sidebar, { SidebarElement } from "./components/Sidebar.vue";

const sidebar: SidebarElement[] = [
  {
    icon: "house",
    text: "Home",
  },
  {
    icon: "comment",
    text: "Announcements",
  },
  {
    icon: "book",
    text: "My courses",
  },
  {
    icon: "chart-simple",
    text: "Stats",
  },
  {
    icon: "gear",
    text: "Settings",
  },
];
</script>

<template>
  <div class="outline">
    <Sidebar :elements="sidebar" />
    <div class="content">
      <!-- This slot is for larger screens -->
      <slot></slot>
    </div>
    <User />
  </div>
  <!-- This slot is for smaller screens -->
  <div class="content-responsive">
    <slot></slot>
  </div>
</template>

<style scoped>
@import "./components/theme.css";

.outline {
  display: flex;
  justify-content: space-between;
  padding: var(--page-padding);
}

@media screen and (max-width: 1000px) {
  .outline {
    display: block;
  }

  .content-responsive {
    text-align: center;
  }

  .content {
    display: none;
  }
}

@media screen and (min-width: 1000px) {
  .content-responsive {
    display: none;
  }
}
</style>
