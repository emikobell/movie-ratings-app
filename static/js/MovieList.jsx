function MovieList() {
  const [movieList, setMovieList] = React.useState([])

  React.useEffect(() => {

    (async function fetchData() {
      const response = await fetch("/movies");
      const parsed = await response.json();
      setMovieList(parsed)
    })()

  }, []);

  return (
    <React.Fragment>
      {movieList.map((movie, index) => {
      
        return (
          <Movie
            key={index}
            title={movie.title}
            overview={movie.overview}
            release_date={movie.release_date}
            poster_path={movie.poster_path} />)
        })}
    </React.Fragment>
  );
}