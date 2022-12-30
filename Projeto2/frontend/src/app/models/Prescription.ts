import { Doctor } from "./Doctor";
import { Patient } from "./Patient";

export class Prescription {
    id: number;
    patient: Patient;
    doctor: Doctor;
    date: string;
    message: string;
  
    constructor(id: number, patient: Patient, doctor: Doctor, date: string, message: string) {
        this.id = id;
        this.patient = patient;
        this.doctor = doctor;
        this.date = date;
        this.message = message;
    }
}