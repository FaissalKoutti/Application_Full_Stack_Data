
function timeDiffCalc(dateFuture, dateNow) {
    let diffInMilliSeconds = Math.abs(dateFuture - dateNow) / 1000;

    // calculate days
    const days = Math.floor(diffInMilliSeconds / 86400);
    diffInMilliSeconds -= days * 86400;

    // calculate hours
    const hours = Math.floor(diffInMilliSeconds / 3600) % 24;
    diffInMilliSeconds -= hours * 3600;

    // calculate minutes
    const minutes = Math.floor(diffInMilliSeconds / 60) % 60;
    diffInMilliSeconds -= minutes * 60;

    let difference = '';
    if (days > 0) {
        difference += (days === 1) ? `${days} day, ` : `${days} days, `;
    }

    difference += (hours === 0 || hours === 1) ? `${hours} hour, ` : `${hours} hours, `;

    difference += (minutes === 0 || hours === 1) ? `${minutes} minutes` : `${minutes} minutes`;

    return difference + ' ago'
}

function getColor(magnitude) {
    var color = 'bg-'

    if(magnitude < 3)
        color += 'success'

    else if(magnitude < 6)
        color += 'warning'

    else
        color += 'danger'

    return color 
}

function getProgressBarValue(magnitude){ return parseInt(magnitude) * 10; }

function EarthquakeCard({earthquake}) {

    if(earthquake === undefined) return <p>Meh</p>
    if(earthquake === null) return <p>Meh null</p>

    const properties = earthquake.properties;
    const progressBarClass = "progress-bar " + getColor(properties.mag)
    const dateEvent = new Date(properties.time)
    const dateToday = new Date()
    const diffDate = timeDiffCalc(dateToday, dateEvent)

    return (
        <>
            <a href="#" className="list-group-item list-group-item-action shadow-sm">
                <div className="d-flex w-100 justify-content-between">
                    <h5 className="mb-1">{properties.title}</h5>
                    <small className="text-muted">Significance at {properties.sig/10}%</small>
                </div>
                <p className="mb-1">{properties.place}</p>
                <div className="progress">
                    <div className={progressBarClass} role="progressbar" style={{ width: getProgressBarValue(properties.mag) + '%' }} aria-valuenow={getProgressBarValue(properties.mag)} aria-valuemin="0" aria-valuemax="100">{properties.mag}</div>
                </div>
                <small className="text-muted">{diffDate}</small>
            </a>
            <br/>
            </>
        );
}

export default EarthquakeCard;