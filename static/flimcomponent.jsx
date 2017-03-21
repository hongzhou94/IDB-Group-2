var generateFilm = React.createClass({
                render: function() {
                  return (<h1>The <b>SWE Awakens</b></h1>);
                }
              });

function Film(props) {
	return <div class="row">
                <div class="col-md-7">
                    <a href="#">
                        <img class="img-responsive" src="{{ planet.img_url }}" alt="" style="width: 700px; height: 300px;">
                    </a>
                </div>
                <div class="col-md-5">
                    <h2>{{ planet.name }}</h2>
                    <ul>
                      <li>Climate: { props.climate }</li>
                      <li>Population: { planet.population }</li>
                      <li>Gravity: { planet.gravity }</li>
                      <li>Terrain: { planet.terrain }</li>
                      <li>Residents: 
                        <ul>
                        </ul>
                      </li>
                      <li>Films:
                        <ul>
                        </ul>
                      </li>
                    </ul>
                    <a class="btn btn-primary" href="{{ url_for('planet', planet_id=index) }}">View<span class="glyphicon glyphicon-chevron-right"></span></a>
                </div>
            </div>
            <!-- /.row -->
            <hr>;
}



{% for index, planet in planets %}
var characterlist = <ul>{% for l in planet.characters %} <li><a href="{{ url_for('character', character_id=l.index) }}">{{ l.description }} </a></li>{% endfor %} </ul>
element film1 = <Film climate = "{{planet.climate}}" characters = characterlist>
ReactDOM.render(React.createElement(generateFilm, null), document.getElementById('content'));
{% endfor %}


