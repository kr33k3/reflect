import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';

import { IonicModule } from '@ionic/angular';

import { MemoryInputComponent } from './memory-input/memory-input.component';
import { ContentInputComponent } from '../content/content-input/content-input.component';

import { ViewPage } from '../view/view.page';
import { MemoryNewComponent } from './memory-new/memory-new.component';
import { TagComponent } from '..//tag/tag.component';
import { NewTagComponent } from '../tag/new-tag/new-tag.component';
import { MemoryViewComponent } from './memory-view/memory-view.component';

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
    ReactiveFormsModule
  ],
  declarations: [ ContentInputComponent, MemoryInputComponent, MemoryNewComponent, TagComponent, NewTagComponent, MemoryViewComponent ],
  entryComponents: [NewTagComponent, MemoryViewComponent]
})
export class MemoryModule {}