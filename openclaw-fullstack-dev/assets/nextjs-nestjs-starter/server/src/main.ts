import { Controller, Get, Module, Post, Body } from '@nestjs/common';
import { NestFactory } from '@nestjs/core';

const items = [{ id: 1, title: 'Stabilize the first vertical slice' }];

@Controller()
class AppController {
  @Get('health')
  health() {
    return { ok: true };
  }

  @Get('api/items')
  listItems() {
    return items;
  }

  @Post('api/items')
  createItem(@Body() body: { title?: string }) {
    const item = { id: items.length + 1, title: String(body?.title || '') };
    items.push(item);
    return item;
  }
}

@Module({ controllers: [AppController] })
class AppModule {}

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(process.env.PORT || 3001);
}

bootstrap();
