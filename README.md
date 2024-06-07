# yes-plotly-host
Simple Heroku app to power yes.plotly.host

<div align="center">
  <a href="https://dash.plotly.com/project-maintenance">
    <img src="https://dash.plotly.com/assets/images/maintained-by-plotly.png" width="400px" alt="Maintained by Plotly">
  </a>
</div>


This site allows [Plotly On-Premise](https://plot.ly/products/on-premise/) admins to verify that they can resolve the https://yes.plotly.host domain.
It's implemented as a dynamic webapp so we can return different content by default to web browsers vs. curl/wget.
