<script setup lang="ts">
import TextButton from "./TextButton.vue";
import Input from "./Input.vue";

const props = defineProps(["title", "inputs", "buttons"]);

export interface FormInput {
  label: string;
  id: string;
  type: string;
}

export interface FormButton {
  text: string;
  color: string;
  event: string;
}
</script>

<template>
  <div class="form">
    <div class="content">
      <span class="title">
        {{ props.title }}
      </span>
      <div>
        <div class="inputs">
          <Input
            v-for="i in inputs"
            :label="`${i.label}`"
            :name="`${i.id}`"
            :id="`${i.id}`"
            :type="`${i.type}`"
          />
        </div>
        <div class="buttons">
          <TextButton
            v-for="b in buttons"
            :text="`${b.text}`"
            :color="`${b.color}`"
            @clicked="$emit(`${b.event}`)"
          />
        </div>
        <div class="footer">
          <slot></slot>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import "./theme.css";

.form .content {
  display: flex;
  justify-content: space-between;
  background-color: var(--background);
  padding: var(--page-padding);
}

.form .title {
  font-size: var(--header-font-size);
}

.form .inputs {
  display: flex;
  flex-direction: column;
}

.form .buttons {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-top: 15px;
}

.form .footer {
  text-align: center;
  margin-top: 15px;
}

@media screen and (max-width: 700px) {
  .form .content {
    flex-direction: column;
    align-items: center;
    padding: 0;
  }

  .form .title {
    margin-bottom: 15px;
  }
}
</style>
