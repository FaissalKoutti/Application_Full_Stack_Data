// Home.js
import React from 'react';
import FeedEarthquakes from './FeedEarthquakes';
import MetricCard from './MetricCard';

function Home() {


  return (
    <div className="container">
      <h2>Feed</h2>
      <br />
      <div className="row">
        <div className="col-8">
          <FeedEarthquakes />
        </div>
        <div className="col-4">
          <MetricCard description={"Earthquakes in the database"} agg_type={"count"}/>
          <MetricCard description={"Earthquakes with 6+ magnitude"} agg_type={"filter"}/>
          <MetricCard description={"Maximum magnitude detected"} agg_type={"max"}/>
          <MetricCard description={"Average magnitude detected"} agg_type={"avg"}/>
        </div>
      </div>
    </div>
  );
}

export default Home;