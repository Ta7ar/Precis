import React from "react";
import {
  Navbar,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  NavbarToggler,
  UncontrolledCollapse,
} from "reactstrap";

const CustomNavbar = () => (
  <Navbar
    color="light"
    light
    expand="sm"
    container="md"
    style={{ marginBottom: "2rem" }}
  >
    <NavbarBrand href="/">Precis</NavbarBrand>
    <NavbarToggler id="navbar-collapse-toggler" />
    <UncontrolledCollapse navbar toggler="#navbar-collapse-toggler">
      <Nav navbar style={{ marginLeft: "auto" }}>
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

export default CustomNavbar;
