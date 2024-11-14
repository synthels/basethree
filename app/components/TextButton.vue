<script setup lang="ts">
const props = defineProps(["text", "color"]);
</script>

<template>
  <a
    class="text-button"
    :style="`background-color: ${props.color}`"
    @click="$emit('clicked')"
  >
    {{ props.text }}
  </a>
</template>

<style scoped>
@import "./theme.css";

.text-button {
  padding: var(--element-padding);
  color: white;
  border-radius: var(--border-radius);
}

.text-button:hover {
  cursor: pointer;
}
</style>
