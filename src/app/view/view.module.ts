import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';
import { MemoryModule } from '../memory/memory.module';


import { IonicModule } from '@ionic/angular';

import { MemoryInputComponent } from '../memory/memory-input/memory-input.component';
import { ContentInputComponent } from '../content/content-input/content-input.component';

import { ViewPage } from './view.page';

const routes: Routes = [
  {
    path: '',
    component: ViewPage
  }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild(routes),
    MemoryModule
  ],
  declarations: [ViewPage],
  entryComponents: [MemoryInputComponent]
})
export class ViewPageModule {}
