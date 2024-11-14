<script setup lang="ts">
const props = defineProps(["label", "id", "type"]);
</script>

<template>
  <label :for="`${props.id}`">{{ label }}</label>
  <input
    class="input"
    :name="`${props.id}`"
    :id="`${props.id}`"
    :type="`${props.type}`"
  />
</template>

<style>
.input {
  padding: var(--element-padding);
  border-radius: var(--border-radius);
  border: none;
}

.input:focus {
  outline: none;
}
</style>
