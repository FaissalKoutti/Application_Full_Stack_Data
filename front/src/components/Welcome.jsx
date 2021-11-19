import UserService from "../services/UserService";

const Welcome = () => (
  <div className="col-lg-8 mx-auto p-3 py-md-5">
  <header className="d-flex align-items-center pb-3 mb-5 border-bottom">
      <a href="/" className="d-flex align-items-center text-dark text-decoration-none">
      <img src="/dsaster.png" alt="" width="40" height="40" className="me-2" />
        <span className="fs-4">DSaster</span>
      </a>
    </header>
  
    <main>
      <h1>Get started with DSaster</h1>
      <p className="fs-5 col-md-8">Discover which earthquakes is affecting the world and keep track of their data with your customized profile.</p>
  
      <div className="mb-5">
        <button onClick={() => UserService.doLogin()} className="btn btn-danger btn-lg px-4">Launch app</button>
      </div>
      </main>
  </div>
)

export default Welcome;