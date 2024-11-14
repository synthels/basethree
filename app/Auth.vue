<script lang="ts" setup>
import Form from "./components/Form.vue";
import { FormInput, FormButton } from "./components/Form.vue";
import { signin } from "./auth";

const inputs: FormInput[] = [
  {
    label: "Username",
    id: "name",
    type: "text",
  },
  {
    label: "Password",
    id: "password",
    type: "password",
  },
];

const buttons: FormButton[] = [
  {
    text: "Sign in",
    color: "var(--primary)",
    event: "signin",
  },
  {
    text: "I forgot my password",
    color: "var(--secondary)",
    event: "forgotpwd",
  },
];
</script>

<template>
  <div class="auth">
    <Form title="Sign in" :inputs="inputs" :buttons="buttons" @signin="signin">
      Don't have an account? <RouterLink to="/signup">Sign up</RouterLink>.
    </Form>
  </div>
</template>
