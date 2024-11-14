<script lang="ts" setup>
import Form from "./components/Form.vue";
import { FormInput, FormButton } from "./components/Form.vue";
import { signup } from "./auth";

const inputs: FormInput[] = [
  {
    label: "Username",
    id: "name",
    type: "text",
  },
  {
    label: "Email",
    id: "email",
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
    text: "Create account",
    color: "var(--primary)",
    event: "signup",
  },
];
</script>

<template>
  <div class="auth">
    <Form
      title="Create an account"
      :inputs="inputs"
      :buttons="buttons"
      @signup="signup"
    >
      Already have an account? <RouterLink to="/auth">Sign in</RouterLink>.
    </Form>
  </div>
</template>
