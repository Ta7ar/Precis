import React from "react";

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
    <div>
      Showing articles for {monthNames[currentDate.getMonth()]}{" "}
      {currentDate.getDate()} , {currentDate.getFullYear()}
    </div>
  );
};

export default DateDisplay;
