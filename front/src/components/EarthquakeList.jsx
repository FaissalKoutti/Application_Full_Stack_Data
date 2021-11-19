import EarthquakeCard from "./EarthquakeCard";

function EarthquakeList({earthquakes}) {

    if(earthquakes === null) return <p>Oops</p>;
    if(earthquakes.length === 0) return <p>Oops</p>;

    return (
        <div className="">
            {earthquakes.map(earthquake => (
              <EarthquakeCard key={earthquake.id} earthquake={earthquake}/>
            ))}
        </div>
    );
}

export default EarthquakeList;