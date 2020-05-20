import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { WorldPatientsPage } from './world-patients.page';

const routes: Routes = [
  {
    path: '',
    component: WorldPatientsPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class WorldPatientsPageRoutingModule {}
