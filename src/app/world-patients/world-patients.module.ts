import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { WorldPatientsPageRoutingModule } from './world-patients-routing.module';

import { WorldPatientsPage } from './world-patients.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    WorldPatientsPageRoutingModule
  ],
  declarations: [WorldPatientsPage]
})
export class WorldPatientsPageModule {}
