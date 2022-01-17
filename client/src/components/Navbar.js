import React from "react";
import {
  Navbar,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  NavbarToggler,
  UncontrolledCollapse,
  Container,
} from "reactstrap";

const CustomNavbar = () => {
  return (
    <Navbar
      color="light"
      light
      expand="sm"
      container="md"
      style={{ marginBottom: "1rem" }}
    >
      <NavbarBrand href="/">Precis</NavbarBrand>
      <NavbarToggler id="navbar-collapse-toggler" />
      <UncontrolledCollapse navbar toggler="#navbar-collapse-toggler">
        <Nav className="me-auto" navbar style={{ marginLeft: "auto" }}>
          <NavItem>
            <NavLink href="/about">About</NavLink>
          </NavItem>
          <NavItem>
            <NavLink href="https://github.com/Ta7ar/Precis">GitHub</NavLink>
          </NavItem>
        </Nav>
      </UncontrolledCollapse>
    </Navbar>
  );
};

export default CustomNavbar;
