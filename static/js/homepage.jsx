function App() {
  return (
    <React.Fragment>
      <h1>Welcome!</h1>

      <h2>Navigation</h2>
      <ul>
        <li>
          <a href="/movies">View all movies</a>
        </li>
        <li>
          <a href="/users">View all users</a>
        </li>
      </ul>
    </React.Fragment>
  );
}

ReactDOM.render(<App />, document.getElementById("app"));
