import { post } from "./fetch";

const getInput = (id: string) => {
  return (document.getElementById(id) as HTMLInputElement)!.value;
};

export const signup = () => {
  const email = getInput("email");
  const username = getInput("name");
  const password = getInput("password");

  post("signup", {
    username: username,
    email: email,
    password: password,
  })
    .then((r) => {
      console.log(r);
    })
    .catch((error) => {
      console.log(error.response);
    });
};

export const signin = () => {
  const username = getInput("name");
  const password = getInput("password");

  post("auth", {
    username: username,
    password: password,
  })
    .then((r) => {
      window.location.href = "/app";
    })
    .catch((error) => {
      console.log(error.response);
    });
};
