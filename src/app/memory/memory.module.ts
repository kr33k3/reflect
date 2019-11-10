import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';

import { IonicModule } from '@ionic/angular';

import { MemoryInputComponent } from './memory-input/memory-input.component';
import { ContentInputComponent } from '../content/content-input/content-input.component';

const routes: Routes = [
   {
     path: '',
     component: MemoryInputComponent
   }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild(routes),
    ReactiveFormsModule
  ],
  declarations: [ ContentInputComponent, MemoryInputComponent ]
})
export class MemoryModule {}