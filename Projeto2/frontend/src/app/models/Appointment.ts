import { Department } from "./Department";
import { Patient } from "./Patient";

export class Appointment {
    id: number;
    patient: Patient;
    department: Department;
    date: string;
    message: string;
  
    constructor(id: number, patient: Patient, department: Department, date: string, message: string) {
        this.id = id;
        this.patient = patient;
        this.department = department;
        this.date = date;
        this.message = message;
    }
}