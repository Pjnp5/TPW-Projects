import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Emitter } from 'src/app/emitters/emitters';
import { User } from 'src/app/models/User';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  private baseURL = environment.API_URL_TEMPLATE;
  private httpOptions = environment.HTTP_OPTIONS;

  constructor(private http: HttpClient) { }

  signup(data: {}): Observable<any> {
    const url = this.baseURL + 'signup';
    return this.http.post(url, data, this.httpOptions);
  }

  login(data: {}): Observable<any> {
    const url = this.baseURL + 'login';
    return this.http.post(url, data, {withCredentials: true});
  }

  logout(): Observable<any> {
    const url = this.baseURL + 'logout';
    return this.http.post(url, this.httpOptions);
  }

  //wip
  getJWTCookie() : string { 
    return document.cookie.split(';').map(c => c.trim()).filter(
      c => {
        return c.substring(0, 4) === `jwt=`;
      }).map(c => {
        return decodeURIComponent(c.substring(4));
      })[0] || ""
  }

  //wip
  isAuthenticated(): void {
    const url = this.baseURL + 'getUser';

    const http_options = {
      withCredentials: true,
      headers: new HttpHeaders({
        'jwt':this.getJWTCookie(),
      })
    };

    if (this.getJWTCookie()) {
      this.http.get(url, http_options).subscribe(
        response => {
          console.log(response);
          Emitter.isAuthenticated.emit(true);
          // If this doesnt work
          const user : User = response as User
          Emitter.userId.emit(user.id);
          // Uncomment this:
          // // ts-ignore
          // Emitter.userId.emit(response["id"]);
        }
      )
    }
  }
}
