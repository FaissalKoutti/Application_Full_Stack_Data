import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import Hub from './Hub';
import Welcome from "./Welcome";

import RenderOnAnonymous from "./RenderOnAnonymous";
import RenderOnAuthenticated from "./RenderOnAuthenticated";

const App = () => (
  <Router>
    <RenderOnAnonymous>
      <Welcome />
    </RenderOnAnonymous>
    <RenderOnAuthenticated>
      <Hub />
    </RenderOnAuthenticated>
  </Router>
);

export default App;
