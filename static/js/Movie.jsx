function Movie(props) {
  return (<div>
    <img width="200px" src={props.poster_path}/>
    <h3>{props.title}</h3>
    <p>{props.overview}</p>
    <p>{props.release_date}</p>
    </div>)
}

