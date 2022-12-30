import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Patient } from 'src/app/models/Patient';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class PatientService {

  private baseURL = environment.API_URL_TEMPLATE;
  private httpOptions = environment.HTTP_OPTIONS;

  constructor(private http: HttpClient) { }

  getAllPatients(): Observable<Patient[]> {
    const url = this.baseURL + 'patients';
    return this.http.get<Patient[]>(url);
  }

  updatePatient(patient: Patient): Observable<any> {
    const url = this.baseURL + 'patient/update/'  + patient.user.id;
    return this.http.put<Patient[]>(url, patient, this.httpOptions);
  }

  getPatient(id: number): Observable<Patient> {
    const url = this.baseURL + 'patient/' + id;
    return this.http.get<Patient>(url);
  }
}
