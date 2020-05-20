import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Weather } from './weather';
import { Patients } from './patients';

@Injectable({
  providedIn: 'root'
})
export class RestService {

  constructor(private http: HttpClient) { }

  serverUrl = 'http://127.0.0.1:5000';
  weatherUrl = 'http://127.0.0.1:5000/weatherReport/';
  patientsUrl = 'http://127.0.0.1:5000/patients/';
  graphEmailUrl = 'http://127.0.0.1:5000/graphEmail';

  read(url: string){
    if (this.serverUrl+url === this.weatherUrl)
    {
      return this.http.get<Weather[]>(this.weatherUrl);
    }
    else if (this.serverUrl+url === this.patientsUrl)
    {
      return this.http.get(this.patientsUrl);
    }
    else
    {
      return this.http.get(this.graphEmailUrl+url);
    }
  }
}
