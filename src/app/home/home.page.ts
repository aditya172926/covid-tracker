import { Component, OnInit } from '@angular/core';
import { RestService } from '../rest.service';
import { Weather } from '../weather';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage implements OnInit {
  headers = ["Day", "Temperature", "Windspeed", "Event"]
  weather: Weather[] = [];

  constructor(private rs: RestService, private route: Router) {}

  ngOnInit() {
    console.log('Weather is requested from server')
    this.rs.read("/weatherReport/")
    .subscribe(
      (response) => 
      {
        this.weather = response[0]["data"];
      },
      (error) =>
      {
        console.log("Data not found"+error);
      }
    )
  }
  setTab(path: string) {
    console.log("The navigation button is clicked");
    this.route.navigate([`/${path}`]);
  }
}
