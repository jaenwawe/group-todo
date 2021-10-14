import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Button from 'react-bootstrap/Button';
import { LinkContainer } from 'react-router-bootstrap';

const linkStyles = {
  margin: '0 0.5em'
};

const AppNavbar = () => {
  return (
    <Navbar bg='light' expand='lg'>
      <Container>
        <Navbar.Brand href='#home'>Group Todo</Navbar.Brand>
        <Navbar.Toggle aria-controls='basic-navbar-nav' />
        <Navbar.Collapse id='basic-navbar-nav'>
          <Nav className='ms-auto'>
            <LinkContainer style={linkStyles} to='/login'>
              <Nav.Link>Login</Nav.Link>
            </LinkContainer>
            <LinkContainer style={linkStyles} to='/signup'>
              <Button>Signup</Button>
            </LinkContainer>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default AppNavbar;
