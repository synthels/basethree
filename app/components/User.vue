<script setup lang="ts">
import { onMounted } from "vue";

onMounted(() => {
  let user = (document.getElementById("user-icon") as HTMLInputElement)!;
  let menu = (document.getElementById("user-menu") as HTMLInputElement)!;

  user.onclick = () => {
    if (menu.style.display === "none" || menu.style.display === "") {
      menu.style.display = "block";
    } else {
      menu.style.display = "none";
    }
  };

  window.addEventListener("click", (e) => {
    // @ts-ignore
    if (!menu.contains(e.target) && !user.contains(e.target)) {
      menu.style.display = "none";
    }
  });
});

const elements = [
  {
    icon: "user",
    text: "Profile",
    href: "/",
    color: "var(--text)",
  },
  {
    icon: "moon",
    text: "Toggle theme",
    handler: "",
    color: "var(--text)",
  },
  {
    icon: "arrow-right-from-bracket",
    text: "Sign out",
    href: "/",
    color: "var(--red)",
  },
];
</script>

<template>
  <div class="user-container">
    <div class="user" id="user-icon" />
    <div class="user-menu" id="user-menu">
      <div class="user-menu-element" v-for="e in elements">
        <span
          :class="`icon fa-solid fa-${e.icon}`"
          :style="`color: ${e.color}`"
          aria-hidden="true"
        />
        <RouterLink
          :to="`${e.href}`"
          @click="e.handler"
          v-if="e.handler != null"
        >
          <span :style="`color: ${e.color}`">
            {{ e.text }}
          </span>
        </RouterLink>
        <span :style="`color: ${e.color}`" v-else>
          {{ e.text }}
        </span>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import "./theme.css";

.user-container {
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  float: right;
}

.user {
  width: 30pt;
  height: 30pt;
  border-radius: 50%;
  background-color: var(--secondary);
  align-self: flex-end;
}

.user:hover {
  cursor: pointer;
}

.user-menu {
  display: none;
  position: absolute;
  align-self: flex-end;
  width: 210pt;
  border-radius: var(--border-radius);
  background-color: var(--secondary);
  margin-top: 35pt;
}

.user-menu-element {
  font-size: var(--navigation-font-size);
  border-radius: var(--border-radius);
  padding: 10pt;
}

.user-menu-element:hover {
  cursor: pointer;
  background-color: var(--tertiary);
}

.icon {
  margin-right: 5px;
}
</style>
