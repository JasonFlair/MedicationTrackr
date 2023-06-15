import React from "react";
import axios from "axios";
import { Redirect } from "react-router-dom";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import {
  StyledForm,
  StyledInput,
  StyledButton,
  StyledAlert,
  StyledLabel,
  StyledContainer,
} from "./FormElements";

const LoginForm = (props) => {
  const { isAuthenticated, setIsAuthenticated } = props;
  const [username, setUsername] = React.useState("");
  const [email, setEmail] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [passwordInvalid, setPasswordInvalid] = React.useState(false);
  const [enabled, setEnabled] = React.useState(false);

  if (isAuthenticated) {
    return <Redirect to="/" />;
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    const formType = window.location.href.split("/").reverse()[0];

    // validate password and set passwordInvalid state accordingly
    if (password.length < 8) {
      setPasswordInvalid(true);
    } else {
      setPasswordInvalid(false);
    }
    let data = {
      email: email,
      password: password,
    };
    if (formType === "register") {
      data.username = username;
    }
    const url = `http://127.0.0.1:5000/${formType}`;
    axios
      .post(url, data)
      .then((res) => {
        setEmail("");
        setUsername("");
        setPassword("");
        setIsAuthenticated(true);
        console.log(res.data.id);
        window.localStorage.setItem("id", res.data.id);
      })
      .catch((err) => console.log(err));
  };

  const emailEntered = (e) => {
    setEmail(e.target.value);
    // buttonEnabled(username, password)
  };

  const usernameEntered = (e) => {
    setUsername(e.target.value);
    // buttonEnabled(username, password)
  };

  const passwordEntered = (e) => {
    setPassword(e.target.value);
    // buttonEnabled(username, password)disabled={!username || !password}
  };

  const showToastMessage = () => {
    toast.success(
      props.formType === "Register" ? "Successfully Register !" : "Successfully Login !",
      {
        position: toast.POSITION.TOP_RIGHT,
      },
      { delay: 1000 }
    );
  };

  return (
    <StyledContainer>
      <StyledForm onSubmit={handleSubmit}>
        <h1>{props.formType === "Register"? "Register New User": "Login User"}</h1>
        {props.formType === "Register" && (
          <>
            <StyledLabel>Username:</StyledLabel>
            <StyledInput
              type="text"
              value={username}
              onChange={(e) => usernameEntered(e)}
            />
          </>
        )}
        <StyledLabel>Email:</StyledLabel>
        <StyledInput
          type="text"
          value={email}
          onChange={(e) => emailEntered(e)}
        />
        <StyledLabel invalid={passwordInvalid}>Password:</StyledLabel>
        <StyledInput
          type="password"
          value={password}
          onChange={(e) => passwordEntered(e)}
        />
        {passwordInvalid && <StyledAlert>Password is invalid.</StyledAlert>}
        <StyledButton onClick={showToastMessage} type="submit">
          {props.formType === "Register" ? "Register" : "Login"}
        </StyledButton>
      </StyledForm>
    </StyledContainer>
  );
};

export default LoginForm;
