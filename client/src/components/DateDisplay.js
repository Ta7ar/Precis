import React from "react";
import { Alert } from "reactstrap";

const DateDisplay = () => {
  const monthNames = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];
  const currentDate = new Date();
  return (
    <Alert color="secondary" style={{ marginTop: "1rem" }}>
      Showing articles for{" "}
      <span style={{ fontWeight: 600 }}>
        {monthNames[currentDate.getMonth()]} {currentDate.getDate()} ,{" "}
        {currentDate.getFullYear()}
      </span>
    </Alert>
  );
};

export default DateDisplay;
