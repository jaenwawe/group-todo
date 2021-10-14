import AppNavbar from './components/layout/AppNavbar';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

const App = () => {
  return (
    <div className='App'>
      <Router>
        <AppNavbar />
        <Switch></Switch>
      </Router>
    </div>
  );
};

export default App;
