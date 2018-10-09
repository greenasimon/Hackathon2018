import React, { Component } from 'react';
import styled from 'styled-components';
import logo from './assets/bookinglogo.png';

const StyledHeader = styled.header`
  background-color: #003580;
  color: white;
  height: 50px;
  padding: 12px 7px;
`;
const Logo = styled.div`
  background: url(${logo}) no-repeat;
  height: 25px;
  background-size: contain;
`;

class Header extends Component {
  render() {
    return (
      <StyledHeader>
        <Logo />
      </StyledHeader>
    );
  }
}

export default Header;
