import { Component, OnInit } from '@angular/core';

declare const $: any;
declare interface RouteInfo {
    path: string;
    title: string;
    icon: string;
    class: string;
}
export const ROUTES: RouteInfo[] = [
  { path: '/dashboard', title: 'Dashboard',  icon: 'dashboard', class: '' },
  { path: '/patient-profiles', title: 'Patient profiles',  icon:'people_outline', class: '' },
  { path: '/patients-list', title: 'Patients List',  icon:'people_outline', class: '' },
  { path: '/user-profile', title: 'Doctor profiles',  icon:'people_outline', class: '' },
  { path: '/table-list', title: 'Doctors List',  icon:'person_add', class: '' },
  { path: '/appointments', title: 'Appointments',  icon:'library_books', class: '' },
  { path: '/create-appointments', title: 'Create Appointments',  icon:'library_books', class: '' },
  { path: '/preprescriptions', title: 'Prescriptions',  icon:'view_list', class: '' }
  
  // { path: '/reports', title: 'Reports',  icon:'view_list', class: '' },
];

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit {
  menuItems: any[];

  constructor() { }

  ngOnInit() {
    this.menuItems = ROUTES.filter(menuItem => menuItem);
  }
  isMobileMenu() {
      if ($(window).width() > 991) {
          return false;
      }
      return true;
  };
}
