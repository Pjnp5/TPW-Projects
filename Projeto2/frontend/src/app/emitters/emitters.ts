import { EventEmitter } from "@angular/core";

export class Emitter {
    // Emits if User is Authenticated
    static isAuthenticated = new EventEmitter<boolean>();
    // Emits the User Id (JWT Token)
    static userId = new EventEmitter<number>();
    // Emits the User Authorizations
    static usertype = new EventEmitter<string>();
}