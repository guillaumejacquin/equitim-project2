import React from "react";
import { useForm, useStep } from "react-hooks-helper";
import Page1 from "../pages/page1";
import Page2 from "../pages/page2";
import Page_beta from "./page_beta";


const defaultData = {
  Nom: "",
  Droit: "",
  nickName: "",
  address: "",
  city: "",
  state: "",
  zip: "",
  phone: "",
  email: "",
};

const steps = [
  { id: "Page1" },
  { id: "Page2" },
  { id: "Page3" },

];

export const MultiStepForm = () => {
  const [formData, setForm] = useForm(defaultData);
  const { step, navigation } = useStep({
    steps,
    initialStep: 0,
  });

  const props = { formData, setForm, navigation};
  switch (step.id) {
    case "Page1":
      return <Page_beta {...props} />;
    case "Page2":
        return <Page2 {...props} />;

    case "Page3":
          return <Page2 {...props} />;
  }
  console.log(step.id)
  return (
    <div>
      <h1>Multi step form</h1>
    </div>
  );
};