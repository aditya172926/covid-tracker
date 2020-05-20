import { Component, OnInit } from '@angular/core';
import { RestService } from '../rest.service';
import { Patients } from '../patients';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-world-patients',
  templateUrl: './world-patients.page.html',
  styleUrls: ['./world-patients.page.scss'],
})
export class WorldPatientsPage implements OnInit {
  headers = ["Coronavirus Cases:", "Deaths:", "Recovered:"];
  patient_units: Patients[] = [];
  text: any;
  Email: string;

  constructor(private rs: RestService, private http: HttpClient) 
  {}

  ngOnInit() {
    this.rs.read("/patients/")
    .subscribe(
      (response) => 
      {
        this.patient_units = response[0]["data"];
      },
      (error) =>
      {
        console.log("No data available"+ error);
      }
    )
  }

  sendGraphEmail(){
    this.rs.read("/"+this.Email)
    .subscribe(
      (response) =>
      {
        this.text = response;
      },
      (error) =>
      {
        console.log('No data');
      }
    )
  }
}
